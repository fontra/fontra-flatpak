# Fontra Flatpak
## Flatpak repository for Fontra

![Fontrapak Screenshot](screenshots/screenshot_02_dark.png)

### Key Features

* **Supported File Formats:**
  * **Read & Write:** Fontra (`.fontra`), Unified Font Object (`.ufo`), DesignSpace (`.designspace`), and RoboFont Component Format (`.rcjk`).
  * **Partial Read & Write:** Glyphs (`.glyphs`, `.glyphspackage`).
  * **Read-Only (Import):** TrueType (`.ttf`), OpenType (`.otf`), WOFF (`.woff`), WOFF2 (`.woff2`), and TTX XML (`.ttx`).
* **Variable Font Native:** Designed from the ground up for multi-axis variable font design, interpolation, and axis management.
* **Modern Vector Editing:** Non-destructive path operations, full component support, custom anchors, and multi-layer editing.
* **Text Shaping & Live Preview:** Real-time text shaping engine with OpenType feature testing.
* **Extensible & Web-Native:** Runs seamlessly in the browser or as a standalone local application via Flatpak.

### Installation

* If Flatpak is not already enabled on your Linux distribution, follow [these instructions](https://flatpak.org/setup/) for your distribution to enable it.
* If Flatpak is integrated with your Software Center (as in Fedora Workstation or Manjaro), download [`xyz.fontra.FontraPak.flatpakref`](https://fontra.github.io/fontra-flatpak/xyz.fontra.FontraPak.flatpakref), right-click it, and select **Open with -> Software Install**.
* Otherwise, copy and paste the following command into your terminal:

```bash
flatpak install --from https://fontra.github.io/fontra-flatpak/xyz.fontra.FontraPak.flatpakref
```
* Type Y for yes and provide your password when prompted
* Fontrapak with all its dependancy will be installed in your computer

### Update

* If Fontrapak is showing in your Software centre, you can press the "Update" button to update to the latest version.
* Otherwise. open your terminal and type
```bash
flatpak update xyz.fontra.FontraPak
```
### Running Fontra Flatpak

* In terminal, start the application by typing
```bash
flatpak run xyz.fontra.FontraPak
```
* Alternatively, open your app menu app menu and click on the Fontra icon <img src="https://fontra.xyz/fontra-icon.svg" alt="Fontra icon" height="32">

### Known Issues 

* **GNOME Wayland Titlebar Decorations:** On GNOME Wayland sessions, window titlebar controls (close, minimize, maximize) may be missing or lack native Adwaita styling depending on your distribution and GNOME version. See [fontra-pak#271](https://github.com/fontra/fontra-pak/issues/271).
* **Performance on Debian Trixie:** The Flatpak build has been reported to run slower on some distributions like Debian 13 (Trixie) compared to the base standalone binary[cite: 1]. We are currently investigating the cause[cite: 1].

---

### Reporting Issues

* **Flatpak packaging or runtime issues:** Open an issue on [fontra-flatpak/issues](https://github.com/fontra/fontra-flatpak/issues).
* **General Linux bugs or application crashes:** Open an issue on [fontra-pak/issues](https://github.com/fontra/fontra-pak/issues).
