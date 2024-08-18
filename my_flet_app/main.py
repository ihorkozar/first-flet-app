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

    progress_ring = ft.ProgressRing(
        value=0.75,  # 75% completion
        width=195,  # Width of the ring
        height=195,  # Height of the ring
        stroke_width=14,  # Thickness of the ring
        color=ft.colors.BLUE,  # Color of
    )

    # Create a Text widget to show the percentage
    percentage_text = ft.Text(
        "75%",
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLUE
    )

    # Stack the ProgressRing and the Text together
    circular_indicator = ft.Stack(
        [
            progress_ring,
            ft.Container(content=percentage_text, alignment=ft.alignment.center)
        ],
        alignment=ft.alignment.center
    )

    # Create the Body (Content area)
    body = ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    padding=ft.Padding(10, 16, 10, 16),
                    content=ft.Row(
                        height=56,
                        alignment=ft.MainAxisAlignment.CENTER,  # Center the row contents
                        spacing=10,
                        controls=[
                            ft.Row(
                                width=80,
                                controls=[
                                    ft.Image(
                                        src="assets/cup.svg",
                                        color="#FAD074",
                                        width=24
                                    ),
                                    ft.Text("100 g", size=14, color="#FAD074")
                                    # Text next to the cup icon
                                ],
                            ),
                            ft.VerticalDivider(width=1, color="#FAD074"),
                            ft.Row(
                                width=80,
                                controls=[
                                    ft.Image(
                                        src="assets/leaf.svg",
                                        color="#FAD074",
                                        width=24
                                    ),
                                    ft.Text("2 g", size=14, color="#FAD074")
                                    # Text next to the leaf icon
                                ],
                            ),
                            ft.VerticalDivider(width=1, color="#FAD074"),
                            ft.Row(
                                width=80,
                                controls=[
                                    ft.Image(
                                        src="assets/icon_water.svg",
                                        color="#FAD074",
                                        width=24
                                    ),
                                    ft.Text("150 ml", size=14, color="#FAD074")
                                    # Text next to the water icon
                                ],
                            ),
                            ft.VerticalDivider(width=1, color="#FAD074"),
                            ft.Row(
                                width=80,
                                controls=[
                                    ft.Image(
                                        src="assets/lid.svg",
                                        color="#FAD074",
                                        width=24
                                    ),
                                    ft.Text("0 g", size=14, color="#FAD074")
                                    # Text next to the lid icon
                                ],
                            ),
                        ]
                    ),
                    border=ft.Border(
                        top=ft.BorderSide(color="#FAD074", width=1),  # Set the top border
                        bottom=ft.BorderSide(color="#FAD074", width=1)  # Set the bottom border
                    )
                ),
                ft.Container(height=45),
                ft.Row(controls=[
                    ft.Column(width=56, controls=[
                        ft.Text("3 /12"),
                        ft.Image(
                            src="assets/icon_water.svg",
                            color="#FAD074",
                            width=24
                        ),
                        ft.Image(
                            src="assets/icon_water.svg",
                            color="#FAD074",
                            width=24
                        ),
                        ft.Image(
                            src="assets/icon_water.svg",
                            color="#FAD074",
                            width=24
                        ),
                        ft.Image(
                            src="assets/icon_water.svg",
                            color="#FAD074",
                            width=24
                        ),
                        ft.Image(
                            src="assets/icon_water.svg",
                            color="#FAD074",
                            width=24
                        ),
                        ft.Image(
                            src="assets/icon_water.svg",
                            color="#FAD074",
                            width=24
                        ),
                        ft.Image(
                            src="assets/icon_water.svg",
                            color="#FAD074",
                            width=24
                        ),
                        ft.Image(
                            src="assets/icon_water.svg",
                            color="#FAD074",
                            width=24
                        ),
                        ft.Image(
                            src="assets/icon_water.svg",
                            color="#FAD074",
                            width=24
                        ),
                        ft.Image(
                            src="assets/icon_water.svg",
                            color="#FAD074",
                            width=24
                        ),
                        ft.Image(
                            src="assets/icon_water.svg",
                            color="#FAD074",
                            width=24
                        ),

                    ]),
                    ft.Column(controls=[
                        circular_indicator,
                        ft.Container(height=106),
                        ft.Image(
                            src="assets/cup-open.png",
                            width=195
                        ),
                    ])
                ]),
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True,
        ),
    )

    # Add AppBar, Body, and FAB to the page
    page.appbar = app_bar
    page.add(body)

    # Update the page
    page.update()


# Run the Flet app
ft.app(target=main)
