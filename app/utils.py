from flask import url_for


def calculate_page_link(page: int, query_string: str) -> str:
    href = f"{url_for('adopt.adopt_page')}?page={page}"
    if query_string:
        href += f"&{query_string}"
    return href
