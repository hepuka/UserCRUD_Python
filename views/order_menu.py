from views.base_menu import BaseMenu
from bson import ObjectId

class OrderMenu(BaseMenu):

    def __init__(self, logged_user, user_controller, product_controller, order_controller):
        super().__init__(logged_user, user_controller, product_controller, order_controller)
        self.logged_user = logged_user
        self.user_controller = user_controller
        self.product_controller = product_controller
        self.order_controller = order_controller

    status_map = {
        "n": "Nyitott",
        "f": "Fizetve",
    }

    category_map = {
        "i": "Ital",
        "p": "Péksütemény",
        "k": "Kávé",
        "g": "Gyümölcslé",
        "t": "Tea",
        "s": "Sütemény"
    }


    def show(self):
        menu = {
            "1": ("Új rendelés felvétele", self.create_order),
            "2": ("Rendelések listázása", self.get_orders),
            "3": ("Rendelés zárása / Fizetés", self.close_order),
            "4": ("Visszalépés a főmenübe", self.back_to_prev_menu),
            "0": ("Kilépés", self.exit_app)
        }
        return self.run(menu, "RENDELÉSEK MENÜ")

    def get_orders(self):
        print("\nRendelés állapota:")
        print("(N) Nyitott")
        print("(F) Fizetve")
        print("Asztalszám (1-5):")
        print("(Enter) Összes")

        status_input = input("Melyik rendelési állapotot szeretnéd megjeleníteni? ").strip().lower()

        if status_input == "":
            orders = self.order_controller.get_all()
        elif status_input in self.status_map:
            orders = self.order_controller.get_by_status(self.status_map[status_input])
        elif status_input == "1" or status_input == "2" or status_input == "3" or status_input == "4" or status_input == "5":
            orders = self.order_controller.get_by_tablenumber(status_input)
        else:
            print("Érvénytelen státusz!")
            return

        if not orders:
            print("\nNincs rögzített rendelés!")
            return

        print("\nRÖGZÍTETT RENDELÉSEK")
        header = (
            f"{'Rendelés ideje'.ljust(20)} | "
            f"{'Rendelés módosítva'.ljust(20)} | "
            f"{'Asztalszám'.ljust(12)} | "
            f"{'Rendelés állapota'.ljust(20)} | "
            f"{'Végösszeg'.ljust(10)} | "
            f"{'Felszolgáló ID'.ljust(24)} | "
            f"Rendelés részletei"
        )
        print(header)
        print("-" * 130)

        for order in orders:

            if hasattr(order, 'products') and order.products:
                products_str = ", ".join(
                    f"{p.get('name', '').capitalize()} x{p.get('quantity', 0)}"
                    for p in order.products
                )
            else:
                products_str = "-"

            print(
                f"{(order.createdAt or '').ljust(20)} | "
                f"{(order.modifiedAt or '-').ljust(20)} | "
                f"{(order.table_number or '').ljust(12)} | "
                f"{(order.status or '').ljust(20)} | "
                f"{(str(order.total) or '0').ljust(10)} | "
                f"{(str(order.user_id) if order.user_id else '').ljust(24)} | "
                f"{products_str}"
            )

    def create_order(self):

        if not isinstance(self.logged_user._id, ObjectId):
            self.logged_user._id = ObjectId(self.logged_user._id)

        tableinput = input("Asztalszám (1-5): ")

        if not tableinput.isdigit() or not (1 <= int(tableinput) <= 5):
            print("Csak 1 és 5 közötti szám adható meg!")
            return

        existing_order = self.order_controller.get_open_order_by_table(tableinput)

        if existing_order:
            print(f"\nLEADOTT RENDELÉSEK: {existing_order.table_number}. ASZTAL:")

            header = (
                f"{'Rendelés ideje'.ljust(20)} | "
                f"{'Rendelés módosítva'.ljust(20)} | "
                f"{'Asztalszám'.ljust(12)} | "
                f"{'Rendelés állapota'.ljust(20)} | "
                f"{'Végösszeg'.ljust(10)} | "
                f"{'Felszolgáló ID'.ljust(24)} | "
                f"Rendelés részletei"
            )
            print(header)
            print("-" * 130)

            if hasattr(existing_order, 'products') and existing_order.products:
                products_str = ", ".join(
                    f"{p.get('name', '').capitalize()} x{p.get('quantity', 0)}"
                    for p in existing_order.products
                )
            else:
                products_str = "-"

            print(
                f"{(existing_order.createdAt or '').ljust(20)} | "
                f"{(existing_order.modifiedAt or '-').ljust(20)} | "
                f"{(existing_order.table_number or '').ljust(12)} | "
                f"{(existing_order.status or '').ljust(20)} | "
                f"{(str(existing_order.total) or '0').ljust(10)} | "
                f"{(str(existing_order.user_id) if existing_order.user_id else '').ljust(24)} | "
                f"{products_str}"
            )

        else:
            print("\nNincs rögzített rendelés az asztalnál")

        print("\nKategóriák:")
        print("(I) Ital")
        print("(P) Péksütemény")
        print("(K) Kávé")
        print("(G) Gyümölcslé")
        print("(T) Tea")
        print("(S) Sütemény")
        print("(Enter) Összes")

        category_input = input("Melyik kategóriát szeretnéd megjeleníteni? ").strip().lower()

        if category_input == "":
            products = self.product_controller.get_all()
        elif category_input in self.category_map:
            products = self.product_controller.get_by_category(self.category_map[category_input])
        else:
            print("Érvénytelen kategória!")
            return

        if not products:
            print("\nNincs rögzített termék ebben a kategóriában!")
            return

        new_products = []
        total_to_add = 0

        print("\nVÁLASZTHATÓ TERMÉKEK:")
        print(
            f"{'#'.ljust(4)} | "
            f"{'Név'.ljust(20)} | "
            f"{'Kategória'.ljust(15)} | "
            f"{'Ár (Ft)'.ljust(10)} | "
            f"{'Kiszerelés'.ljust(15)}"
        )
        print("-" * 70)

        for index, product in enumerate(products, start=1):
            print(
                f"{str(index).ljust(4)} | "
                f"{product.name.capitalize().ljust(20)} | "
                f"{product.category.ljust(15)} | "
                f"{str(product.price).ljust(10)} | "
                f"{product.packaging.ljust(15)}"
            )

        while True:

            choice = input("\nAdd meg a termék számát (Enter = kész): ").strip()

            if choice == "":
                break

            if not choice.isdigit():
                print("Számot adj meg!")
                continue

            index = int(choice) - 1

            if index < 0 or index >= len(products):
                print("Érvénytelen sorszám!")
                continue

            selected_product = products[index]

            print(f"\nVálasztott termék: {selected_product.name.capitalize()}")

            quantity = int(input("Mennyiség: "))

            if quantity <= 0:
                print("Érvénytelen mennyiség!")
                continue

            unit_price = int(selected_product.price)
            total_price = unit_price * quantity

            order_item = {
                "product": selected_product.get_id(),
                "name": selected_product.name,
                "quantity": quantity,
                "unit_price": unit_price,
                "total_price": total_price
            }

            new_products.append(order_item)
            total_to_add += total_price

            print(f"Hozzáadva: {selected_product.name} x{quantity}")

        if not new_products:
            print("Nem választottál terméket!")
            return

        if existing_order:

            success=self.order_controller.add_products_to_order(
                existing_order._id,
                new_products,
                total_to_add
            )

            if success:
                print("\nA rendelés sikeresen frissítve!")
            else:
                print("A rendelés nem található!")

        else:

            order_data = {
                "user_id": self.logged_user._id,
                "table_number": tableinput,
                "products": new_products,
                "total": total_to_add,
                "status": "nyitott",
            }

            self.order_controller.create(order_data)

            print("\nRendelés sikeresen létrehozva!")

    def close_order(self):
        table_input = input("Melyik asztal rendelését szeretnéd lezárni? ").strip()

        if table_input not in ["1", "2", "3", "4", "5"]:
            print("Érvénytelen asztalszám!")
            return

        orders = self.order_controller.get_by_tablenumber(table_input)

        if not orders:
            print("\nNincs rögzített rendelés ennél az asztalnál!")
            return

        # Nyitott rendelés kiválasztása
        open_orders = [o for o in orders if o.status.lower() == "nyitott"]
        if not open_orders:
            print("Nincs nyitott rendelés az asztalnál!")
            return

        for order in open_orders:
            print(f"\nRendelés ID: {order._id}, Asztal: {order.table_number}, Összeg: {order.total} Ft")
            confirm = input("Biztosan lezárod ezt a rendelést? (i/n): ").strip().lower()
            if confirm == "i":
                success = self.order_controller.close_order(order._id)
                if success:
                    print(f"A rendelés ({order._id}) sikeresen lezárva és fizetve!")
                else:
                    print("Hiba történt a rendelés lezárásakor.")
            else:
                print("Rendelés lezárása megszakítva.")