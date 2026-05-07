from pages.home_page import Homepage
from pages.product_listing_page import ProductListingPage


def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'Url for amazon is not correct'
    print("\nOpened Amazon Homepage. Title & URL verified")

def test_search_product(driver):
    homepage = Homepage(driver)
    homepage.type_search_input()
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded() == True, 'Search results page did not load'
    print("\n Search results page loaded successfully.")

def test_find_elements_amazon(driver):
    productlistingpage = ProductListingPage(driver)

    productlistingpage.find_product_title()
    val = productlistingpage.all_products()

    assert val, "No products found on Amazon search results"

def test_brand_filter(driver):
    productlistingpage = ProductListingPage(driver)
    productlistingpage.select_brand_filter()

    assert productlistingpage.check_product_titles_for_brand_filter('Logitech'), 'Brand filter did not apply'


