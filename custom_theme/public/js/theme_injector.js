

frappe.after_ajax(() => {
  frappe.call({
    method: "custom_theme.utils.get_theme_colors",
    callback: function (r) {
      if (!r.message) return;

      const {
        primary_color,
        input_background_color,
        button_primary_color,
        button_secondary_color,
        navbar,
      } = r.message;

      const style = document.createElement('style');
      style.innerHTML = `
        :root {
          --primary-color: ${primary_color};
          --input-bg-color: ${input_background_color};
          --button-primary-color: ${button_primary_color};
          --button-secondary-color: ${button_secondary_color};
          --navbar:${navbar};
        }
      `;
      document.head.appendChild(style);
    }
  });
});
