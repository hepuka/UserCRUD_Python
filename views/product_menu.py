from views.base_menu import BaseMenu
class ProductView(BaseMenu):

    def show(self):
        menu = {
            "1": ("Új termékregisztráció", self.add_product),
            "2": ("Termék keresése", self.get_product),
            "3": ("Termékek listázása", self.get_products),
            "4": ("Termék adatainak módosítása", self.edit_product),
            "5": ("Termék törlése", self.delete_product),
            "6": ("Visszalépés a főmenübe", self.back_to_prev_menu),
            "0": ("Kilépés", self.exit_app)
        }

        return self.run(menu, "TERMÉKMENÜ")

    def add_product(self):
        name = input("Név: ")
        tmp = input("Kategória: (I)Ital (P)Péksütemény (K)Kávé (G)Gyümölcslé (T)Tea (S)Sütemény:")
        category = None
        price = input("Ár: ")
        packaging = input("Kiszerelés: ")

        match tmp.lower():
            case "i":
                category = "Ital"
            case "p":
                category = "Péksütemény"
            case "k":
                category = "Kávé"
            case "g":
                category = "Gyümölcslé"
            case "t":
                category = "Tea"
            case "s":
                category = "Sütemény"
            case _:
                ""

        self.product_controller.create({
            "name": name.lower(),
            "category": category,
            "price": price,
            "packaging": packaging,
        })

        print("Termék sikeresen létrehozva!")

    def get_products(self):
        print("\nKategóriák:")
        print("(I) Ital")
        print("(P) Péksütemény")
        print("(K) Kávé")
        print("(G) Gyümölcslé")
        print("(T) Tea")
        print("(S) Sütemény")
        print("(Enter) Összes")

        category_input = input("Melyik kategóriát szeretnéd megjeleníteni? ").strip().lower()

        category_map = {
            "i": "Ital",
            "p": "Péksütemény",
            "k": "Kávé",
            "g": "Gyümölcslé",
            "t": "Tea",
            "s": "Sütemény"
        }

        if category_input == "":
            products = self.product_controller.get_all()
        elif category_input in category_map:
            products = self.product_controller.get_by_category(category_map[category_input])
        else:
            print("Érvénytelen kategória!")
            return

        if not products:
            print("\nNincs rögzített termék ebben a kategóriában!")
            return

        print("\nRÖGZÍTETT TERMÉKEK")
        print(
            f"{'Név'.ljust(20)} | "
            f"{'Kategória'.ljust(20)} | "
            f"{'Ár'.ljust(20)} | "
            f"{'Kiszerelés'.ljust(20)} | "
            f"{'Létrehozva'.ljust(20)} | "
            f"{'Módosítva'.ljust(20)}"
        )

        print("-" * 135)

        for product in products:
            print(
                f"{(product.name.capitalize() or '').ljust(20)} | "
                f"{(product.category or '').ljust(20)} | "
                f"{(product.price or '').ljust(20)} | "
                f"{(product.packaging or '').ljust(20)} | "
                f"{(product.createdAt or '').ljust(20)} | "
                f"{(product.modifiedAt or '-').ljust(20)}"
            )

    def get_product(self):
        keyword = input("Add meg a termék nevét: ").lower()

        products = self.product_controller.search_products(keyword)

        if not products:
            print("Nincs találat!")
            return

        print("\n--- RÖGZÍTETT TERMÉKEK ---")

        for product in products:
            print(f"Név: {product.name.capitalize()}")
            print(f"Kategória: {product.category}")
            print(f"Ár: {product.price}")
            print(f"Kiszerelés: {product.packaging}")
            print(f"Létrehozva: {product.createdAt}")
            print(f"Módosítva: {product.modifiedAt or '-'}\n")

    def edit_product(self):
        product_tmp = input("Add meg a termék nevét: ").lower()
        product = self.product_controller.get_product(product_tmp)

        if not product:
            print("Termék nem található!")
            return

        print("\n--- Termék adatainak módosítása ---")
        print("(Enter = a megadott adat változatlan marad)\n")

        name = input(f"Név [{product.name}]: ").strip()
        price = input(f"Ár [{product.price}]: ").strip()
        packaging = input(f"Kiszerelés [{product.packaging}]: ").strip()

        self.product_controller.update_product(product, name.lower(), price, packaging)
        print("Termék adatai sikeresen módosítva!")

    def delete_product(self):
        product = input("Add meg a törlendő termék nevét: ")
        tmp = input("Biztosan törölni szeretnéd a felhasználót? (I) Igen (N) Mégsem: ").lower()

        if tmp == "i":
            self.product_controller.delete("name", product)
            print("Termék sikeresen törölve")
            return
        else:
            print("Termék törlése megszakítva.")
            return