/* ============================================================
   HELPDESK · MAIN.JS
   ------------------------------------------------------------
   Todo el código está envuelto en una IIFE (Immediately
   Invoked Function Expression) para NO contaminar el
   scope global. Solo hay 4 funciones, una por característica:

     1) initAutoSubmitFilters  → filtra al cambiar un <select>
     2) initAlertClose         → botón X en alertas
     3) initAutoDismissAlerts  → cierra alertas a los 5s
     4) initFormValidation     → validación del form de crear

   ¿Cómo modificarlo?
     - Para que las alertas duren más: cambia 5000 a 8000.
     - Para desactivar el filtro automático: comenta la línea
       del initAutoSubmitFilters() en DOMContentLoaded.
     - Para validar más reglas, edita initFormValidation.
============================================================ */
(function () {
    "use strict";   // activa modo estricto de JS (evita errores silenciosos)

    /* -------------------------------------------------------
       PUNTO DE ENTRADA
       Esperamos a que el DOM esté listo antes de buscar
       elementos. Si lo hiciéramos antes, no encontraríamos
       nada porque aún no existen.
    ------------------------------------------------------- */
    document.addEventListener("DOMContentLoaded", function () {
        initAutoSubmitFilters();
        initAlertClose();
        initAutoDismissAlerts();
        initFormValidation();
    });

    /* ============================================================
       1) AUTO-SUBMIT DE FILTROS
       ------------------------------------------------------------
       Cuando el usuario cambia cualquiera de los <select>
       dentro del formulario con id="filters-form", enviamos
       el formulario automáticamente.
       Así el usuario no tiene que pulsar "Filtrar".
       ============================================================ */
    function initAutoSubmitFilters() {
        const form = document.getElementById("filters-form");
        if (!form) return;   // si no hay filtros en esta página, salimos

        // querySelectorAll devuelve todos los <select> del form
        form.querySelectorAll("select").forEach(function (select) {
            select.addEventListener("change", function () {
                form.submit();   // envía el GET a la misma URL
            });
        });
    }

    /* ============================================================
       2) BOTÓN CERRAR EN ALERTAS
       ------------------------------------------------------------
       Cada alerta tiene una <button class="alert-close">×</button>.
       Al hacer clic, se anima el fade-out y se elimina del DOM.
       ============================================================ */
    function initAlertClose() {
        document.querySelectorAll(".alert-close").forEach(function (btn) {
            btn.addEventListener("click", function () {
                // closest() sube por el árbol hasta encontrar el .alert padre
                const alert = btn.closest(".alert");
                if (alert) fadeOutAndRemove(alert);
            });
        });
    }

    /* ============================================================
       3) AUTO-DISMISS DE ALERTAS
       ------------------------------------------------------------
       Después de 5 segundos, cada alerta se cierra sola.
       Si prefieres que se queden hasta que el usuario las cierre,
       comenta la llamada a initAutoDismissAlerts() arriba.
       ============================================================ */
    function initAutoDismissAlerts() {
        document.querySelectorAll(".alert").forEach(function (alert) {
            setTimeout(function () {
                fadeOutAndRemove(alert);
            }, 5000);  // 5000 ms = 5 segundos
        });
    }

    /* ------------------------------------------------------------
       FUNCIÓN AUXILIAR
       Aplica una transición CSS de opacidad + desplazamiento,
       y elimina el elemento del DOM al terminar (260 ms,
       para que no se corte la animación).
    ------------------------------------------------------------ */
    function fadeOutAndRemove(el) {
        el.style.transition = "opacity .25s ease, transform .25s ease";
        el.style.opacity = "0";
        el.style.transform = "translateY(-6px)";
        setTimeout(function () { el.remove(); }, 260);
    }

    /* ============================================================
       4) VALIDACIÓN DE FORMULARIOS
       ------------------------------------------------------------
       Solo actúa sobre <form novalidate> (así no choca con
       la validación nativa del navegador).
       Reglas:
         - Todo campo con [required] no puede estar vacío.
         - Si falla, añade .has-error al .form-group padre y
           escribe el mensaje en el <small data-error-for>.
         - Al escribir en el campo, se limpia el error.
       ============================================================ */
    function initFormValidation() {
        // Recorremos todos los formularios con novalidate
        document.querySelectorAll("form[novalidate]").forEach(function (form) {

            // ---- Al intentar enviar ----
            form.addEventListener("submit", function (e) {
                let valid = true;

                // Buscamos todos los campos obligatorios
                form.querySelectorAll("[required]").forEach(function (field) {
                    const group = field.closest(".form-group");
                    const errorEl = group
                        ? group.querySelector("[data-error-for]")
                        : null;

                    // .trim() quita espacios; si queda vacío → error
                    if (!field.value.trim()) {
                        valid = false;
                        if (group) group.classList.add("has-error");
                        if (errorEl) {
                            errorEl.textContent = "Este campo es obligatorio.";
                        }
                    } else {
                        // Si está bien, limpiamos el error por si acaso
                        if (group) group.classList.remove("has-error");
                        if (errorEl) errorEl.textContent = "";
                    }
                });

                // Si algo falla, cancelamos el envío y hacemos scroll
                // al primer campo con error
                if (!valid) {
                    e.preventDefault();
                    const firstError = form.querySelector(".has-error");
                    if (firstError) {
                        firstError.scrollIntoView({
                            behavior: "smooth",
                            block: "center"
                        });
                    }
                }
            });

            // ---- Al escribir, limpiar el error del campo ----
            form.querySelectorAll("[required]").forEach(function (field) {
                field.addEventListener("input", function () {
                    const group = field.closest(".form-group");
                    if (group && group.classList.contains("has-error")) {
                        group.classList.remove("has-error");
                        const errorEl = group.querySelector("[data-error-for]");
                        if (errorEl) errorEl.textContent = "";
                    }
                });
            });
        });
    }
})();