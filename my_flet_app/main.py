import flet as ft


def main(page: ft.Page):
    # Set the title of the app
    page.title = "Flet Scaffold Example"
    page.bgcolor = "#272726"

    # Create an AppBar
    app_bar = ft.AppBar(
        title=ft.Text("New set"),
        center_title=True,
        bgcolor="#272726",
        leading=ft.Image(
            src="assets/back.svg",
        ),
        actions=[
            ft.Image(
                src="assets/more.svg",
            ),
        ],
    )

    # Create the Body (Content area)
    body = ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                src="assets/cup.svg",
                            ),
                            ft.Image(
                                src="assets/leaf.svg",
                            ),
                            ft.Image(
                                src="assets/icon_water.svg",
                                color="#FAD074"
                            ),
                            ft.Image(
                                src="assets/lid.svg",
                            ),
                        ]
                    ),
                    border=ft.Border(
                        top=ft.BorderSide(color="yellow", width=2),  # Set the top border
                        bottom=ft.BorderSide(color="yellow", width=2)  # Set the bottom border
                    )
                ),
                ft.Text("Welcome to my app!", size=30),
                ft.Text("This is a simple scaffold example.", size=20),
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True,
        ),
        padding=20,
    )

    # Add AppBar, Body, and FAB to the page
    page.appbar = app_bar
    page.add(body)

    # Update the page
    page.update()


# Run the Flet app
ft.app(target=main)
