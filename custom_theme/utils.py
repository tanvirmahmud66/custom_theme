# custom_theme/custom_theme/utils.py

import frappe

@frappe.whitelist()
def get_theme_colors():
    settings = frappe.get_single("Theme Settings")
    
    frappe.response['message'] = {
        "primary_color": settings.primary_color or "#54a2fa",
        "input_background_color": settings.input_background_color or "#e6e6e6"
    }
