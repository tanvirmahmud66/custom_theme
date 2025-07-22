# custom_theme/custom_theme/utils.py

import frappe

@frappe.whitelist()
def get_theme_colors():
    settings = frappe.get_single("Theme Settings")
    
    frappe.response['message'] = {
        "primary_color": settings.primary_color or "#54a2fa",
        "input_background_color": settings.input_background_color or "#e6e6e6",
        "button_primary_color": settings.button_primary_color or "#000000",
        "button_secondary_color":settings.button_secondary_color or "#3D3D3D",
        "navbar":settings.navbar or "#eeeeee",
        "navbar_breadcrumb":settings.navbar_breadcrumb or "#000000",
    }
