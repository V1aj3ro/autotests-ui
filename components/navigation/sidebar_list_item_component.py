from typing import Pattern

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = page.get_by_test_id(f'{identifier}-drawer-list-item-icon')
        self.title = page.get_by_test_id(f'{identifier}-drawer-list-item-title-text')
        self.button = page.get_by_test_id(f'{identifier}-drawer-list-item-button')

    def check_visible(self, title: str):
        expect(self.icon).to.be.visible()
        expect(self.title).to.have.text(title)

        expect(self.button).to.be.visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)

