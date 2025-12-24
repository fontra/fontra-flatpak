# Fontra FlatPak
## Flatpak repository for Fontra
![Fontrapak Screenshot](screenshot1.png)

### Installation 
* If Flatpak is already not enabled in your Linux distro, follow [these instructions](https://flatpak.org/setup/) for you distribution to enable it.
* If Flatpak is integrated with your Software Centre (as in Fedora Workstation, Monjaro), just download [this file](https://fontra.github.io/fontra-flatpak/xyz.fontra.FontraPak.flatpakref) , then right click it, and select "Open with -> Software Install" .
* Otherwise, copy and paste the following command in your terminal

```
flatpak install --from https://fontra.github.io/fontra-flatpak/xyz.fontra.FontraPak.flatpakref
```
* Type Y for yes and provide your password when prompted
* Fontrapak with all its dependancy will be installed in your computer

### Update
* If Fontrapak is showing in your Software centre, you can press the "Update" button to update to the latest version.
* Otherwise. open your terminal and type
```
flatpak update xyz.fontra.FontraPak
```
### Running Fontra Flatpak
* In terminal, start the application by typing
```
flatpak run xyz.fontra.FontraPak
```
* Alternatively, open your app menu app menu and click on the Fontra icon
* 
  ![Fontra icon](https://fontra.xyz/fontra-icon.svg)
  
### Known Issues 
 The flatpak is reported to be working slowly in some distros like Debian Trixie where the base Ubuntu binary is working fine. We are currently investigating the issue.
 
For any other problem, please [open an Issue](https://github.com/fontra/fontra-flatpak/issues)
