#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v20
# autospec commit: f35655a
#
Name     : pypi-xpra
Version  : 6.2.1
Release  : 80
URL      : https://files.pythonhosted.org/packages/80/6f/3f96194c9a5d3c458680025f116d4de3dafaea4435997a547003b3b8e30c/xpra-6.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/80/6f/3f96194c9a5d3c458680025f116d4de3dafaea4435997a547003b3b8e30c/xpra-6.2.1.tar.gz
Summary  : runs X clients, typically on a remote host, and directs their display to the local machine without losing any state.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GPL-2.0 GPL-2.0+ GPL-3.0 LGPL-2.0 LGPL-2.1+ LGPL-2.1-only LGPL-3.0 LGPL-3.0+ MIT MPL-1.1 Python-2.0
Requires: pypi-xpra-bin = %{version}-%{release}
Requires: pypi-xpra-config = %{version}-%{release}
Requires: pypi-xpra-data = %{version}-%{release}
Requires: pypi-xpra-libexec = %{version}-%{release}
Requires: pypi-xpra-license = %{version}-%{release}
Requires: pypi-xpra-man = %{version}-%{release}
Requires: pypi-xpra-python = %{version}-%{release}
Requires: pypi-xpra-python3 = %{version}-%{release}
BuildRequires : Linux-PAM
BuildRequires : Linux-PAM-dev
BuildRequires : brotli-dev
BuildRequires : buildreq-distutils3
BuildRequires : libdrm-dev
BuildRequires : libvpx-dev
BuildRequires : libwebp-dev
BuildRequires : not-ffmpeg-dev
BuildRequires : pandoc
BuildRequires : pkgconfig(gdk-3.0)
BuildRequires : pkgconfig(liblz4)
BuildRequires : pkgconfig(libxxhash)
BuildRequires : pkgconfig(py3cairo)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xres)
BuildRequires : pkgconfig(xtst)
BuildRequires : pypi(cython)
BuildRequires : pypi(setuptools)
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
A Fake CUDA RPM do allow us to build python-pycuda against non-RPM versions of CUDA.

%package bin
Summary: bin components for the pypi-xpra package.
Group: Binaries
Requires: pypi-xpra-data = %{version}-%{release}
Requires: pypi-xpra-libexec = %{version}-%{release}
Requires: pypi-xpra-config = %{version}-%{release}
Requires: pypi-xpra-license = %{version}-%{release}

%description bin
bin components for the pypi-xpra package.


%package config
Summary: config components for the pypi-xpra package.
Group: Default

%description config
config components for the pypi-xpra package.


%package data
Summary: data components for the pypi-xpra package.
Group: Data

%description data
data components for the pypi-xpra package.


%package doc
Summary: doc components for the pypi-xpra package.
Group: Documentation
Requires: pypi-xpra-man = %{version}-%{release}

%description doc
doc components for the pypi-xpra package.


%package libexec
Summary: libexec components for the pypi-xpra package.
Group: Default
Requires: pypi-xpra-config = %{version}-%{release}
Requires: pypi-xpra-license = %{version}-%{release}

%description libexec
libexec components for the pypi-xpra package.


%package license
Summary: license components for the pypi-xpra package.
Group: Default

%description license
license components for the pypi-xpra package.


%package man
Summary: man components for the pypi-xpra package.
Group: Default

%description man
man components for the pypi-xpra package.


%package python
Summary: python components for the pypi-xpra package.
Group: Default
Requires: pypi-xpra-python3 = %{version}-%{release}

%description python
python components for the pypi-xpra package.


%package python3
Summary: python3 components for the pypi-xpra package.
Group: Default
Requires: python3-core
Requires: pygobject-python3
Requires: pypi(pillow)

%description python3
python3 components for the pypi-xpra package.


%prep
%setup -q -n xpra-6.2.1
cd %{_builddir}/xpra-6.2.1
pushd ..
cp -a xpra-6.2.1 buildavx2
popd

%build
## build_prepend content
export CPPFLAGS="${CPPFLAGS} -I/usr/include"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1730206823
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
## build_prepend content
export CPPFLAGS="${CPPFLAGS} -I/usr/include"
## build_prepend end
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 setup.py build

popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-xpra
cp %{_builddir}/xpra-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-xpra/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/xpra-%{version}/packaging/debian/xpra/copyright %{buildroot}/usr/share/package-licenses/pypi-xpra/c722dc46afe54071fb7d5c3f48ef46f4b54cafee || :
cp %{_builddir}/xpra-%{version}/xpra/gtk/notifier-LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-xpra/f45ee1c765646813b442ca58de72e20a64a7ddba || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib/sysusers.d/xpra.conf
rm -f %{buildroot}*/lib/systemd/system/xpra.*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib/cups/backend/xpraforwarder

%files bin
%defattr(-,root,root,-)
/usr/bin/run_scaled
/usr/bin/xpra
/usr/bin/xpra_Xdummy
/usr/bin/xpra_launcher

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/xpra.conf
/usr/lib/udev/rules.d/71-xpra-virtual-pointer.rules

%files data
%defattr(-,root,root,-)
/usr/share/applications/xpra-gui.desktop
/usr/share/applications/xpra-launcher.desktop
/usr/share/applications/xpra-shadow.desktop
/usr/share/applications/xpra.desktop
/usr/share/gnome-shell/extensions/input-source-manager@xpra_org/COPYING
/usr/share/gnome-shell/extensions/input-source-manager@xpra_org/README.md
/usr/share/gnome-shell/extensions/input-source-manager@xpra_org/extension.js
/usr/share/gnome-shell/extensions/input-source-manager@xpra_org/metadata.json
/usr/share/icons/xpra-mdns.png
/usr/share/icons/xpra-shadow.png
/usr/share/icons/xpra.png
/usr/share/metainfo/xpra.appdata.xml
/usr/share/mime-packages/application-x-xpraconfig.xml
/usr/share/xpra/COPYING
/usr/share/xpra/README.md
/usr/share/xpra/autostart.desktop
/usr/share/xpra/bell.wav
/usr/share/xpra/css/10_header_bar.css
/usr/share/xpra/css/20_progress_bar.css
/usr/share/xpra/icons/audio.png
/usr/share/xpra/icons/authentication.png
/usr/share/xpra/icons/bandwidth_limit.png
/usr/share/xpra/icons/bell.png
/usr/share/xpra/icons/browse.png
/usr/share/xpra/icons/browser.png
/usr/share/xpra/icons/bugs.png
/usr/share/xpra/icons/clipboard.png
/usr/share/xpra/icons/close.png
/usr/share/xpra/icons/compressed.png
/usr/share/xpra/icons/connect.png
/usr/share/xpra/icons/cross.png
/usr/share/xpra/icons/disconnected.png
/usr/share/xpra/icons/display.png
/usr/share/xpra/icons/documentation.png
/usr/share/xpra/icons/download.png
/usr/share/xpra/icons/empty.png
/usr/share/xpra/icons/encoding.png
/usr/share/xpra/icons/eye-off.png
/usr/share/xpra/icons/eye-on.png
/usr/share/xpra/icons/features.png
/usr/share/xpra/icons/fluxbox.png
/usr/share/xpra/icons/font.png
/usr/share/xpra/icons/forward.png
/usr/share/xpra/icons/freebsd.png
/usr/share/xpra/icons/gnome-session.png
/usr/share/xpra/icons/gnome.png
/usr/share/xpra/icons/gstreamer.png
/usr/share/xpra/icons/information.png
/usr/share/xpra/icons/kde.png
/usr/share/xpra/icons/keyboard.png
/usr/share/xpra/icons/linux.png
/usr/share/xpra/icons/list.png
/usr/share/xpra/icons/lxde.png
/usr/share/xpra/icons/macos.png
/usr/share/xpra/icons/matchbox.png
/usr/share/xpra/icons/maximize.png
/usr/share/xpra/icons/mdns.png
/usr/share/xpra/icons/microphone.png
/usr/share/xpra/icons/minimize.png
/usr/share/xpra/icons/noicon.png
/usr/share/xpra/icons/open.png
/usr/share/xpra/icons/openbox.png
/usr/share/xpra/icons/openbsd.png
/usr/share/xpra/icons/opengl.png
/usr/share/xpra/icons/package.png
/usr/share/xpra/icons/picture.png
/usr/share/xpra/icons/pointer.png
/usr/share/xpra/icons/printer.png
/usr/share/xpra/icons/python.png
/usr/share/xpra/icons/qr.png
/usr/share/xpra/icons/quit.png
/usr/share/xpra/icons/raise.png
/usr/share/xpra/icons/reinitialize.png
/usr/share/xpra/icons/retry.png
/usr/share/xpra/icons/sawfish.png
/usr/share/xpra/icons/scaling.png
/usr/share/xpra/icons/screenshot.png
/usr/share/xpra/icons/server-connected.png
/usr/share/xpra/icons/server-notconnected.png
/usr/share/xpra/icons/server.png
/usr/share/xpra/icons/shadow.png
/usr/share/xpra/icons/shutdown.png
/usr/share/xpra/icons/slider.png
/usr/share/xpra/icons/speaker-off.png
/usr/share/xpra/icons/speaker.png
/usr/share/xpra/icons/speed.png
/usr/share/xpra/icons/sqlite.png
/usr/share/xpra/icons/start.png
/usr/share/xpra/icons/statistics.png
/usr/share/xpra/icons/ticked-small.png
/usr/share/xpra/icons/ticked.png
/usr/share/xpra/icons/timer.png
/usr/share/xpra/icons/toolbox.png
/usr/share/xpra/icons/transfer.png
/usr/share/xpra/icons/transparent.png
/usr/share/xpra/icons/unticked-small.png
/usr/share/xpra/icons/unticked.png
/usr/share/xpra/icons/update.png
/usr/share/xpra/icons/upload.png
/usr/share/xpra/icons/user.png
/usr/share/xpra/icons/video.png
/usr/share/xpra/icons/webcam.png
/usr/share/xpra/icons/win32.png
/usr/share/xpra/icons/windowmaker.png
/usr/share/xpra/icons/windows.png
/usr/share/xpra/icons/xpra.png
/usr/share/xpra/icons/xterm.png
/usr/share/xpra/images/gradient.webp
/usr/share/xpra/images/pinwheel.jpg
/usr/share/xpra/images/smpte-rp-219.png
/usr/share/xpra/images/warning.png

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/xpra/Build/Debian.html
/usr/share/doc/xpra/Build/Dependencies.html
/usr/share/doc/xpra/Build/MSWindows.html
/usr/share/doc/xpra/Build/MacOS.html
/usr/share/doc/xpra/Build/Other.html
/usr/share/doc/xpra/Build/Packaging.html
/usr/share/doc/xpra/Build/RPM.html
/usr/share/doc/xpra/Build/graphs/all.png
/usr/share/doc/xpra/Build/graphs/codecs.png
/usr/share/doc/xpra/Build/graphs/gtk3.png
/usr/share/doc/xpra/Build/graphs/packaging-tools.png
/usr/share/doc/xpra/Build/graphs/python3.png
/usr/share/doc/xpra/Build/graphs/tools.png
/usr/share/doc/xpra/Build/index.html
/usr/share/doc/xpra/CHANGELOG.html
/usr/share/doc/xpra/FAQ.html
/usr/share/doc/xpra/Features/Audio.html
/usr/share/doc/xpra/Features/Clipboard.html
/usr/share/doc/xpra/Features/DPI.html
/usr/share/doc/xpra/Features/Display.html
/usr/share/doc/xpra/Features/File-Transfers.html
/usr/share/doc/xpra/Features/Image-Depth.html
/usr/share/doc/xpra/Features/Keyboard-Shortcut-Window.png
/usr/share/doc/xpra/Features/Keyboard.html
/usr/share/doc/xpra/Features/Notifications.html
/usr/share/doc/xpra/Features/Printing.html
/usr/share/doc/xpra/Features/System-Tray.html
/usr/share/doc/xpra/Features/Webcam.html
/usr/share/doc/xpra/Features/index.html
/usr/share/doc/xpra/Network/AES.html
/usr/share/doc/xpra/Network/Encryption.html
/usr/share/doc/xpra/Network/Multicast-DNS.html
/usr/share/doc/xpra/Network/Protocol.html
/usr/share/doc/xpra/Network/QUIC.html
/usr/share/doc/xpra/Network/SSH.html
/usr/share/doc/xpra/Network/SSL.html
/usr/share/doc/xpra/Network/index.html
/usr/share/doc/xpra/SECURITY.html
/usr/share/doc/xpra/SPONSORS.html
/usr/share/doc/xpra/Subsystems/Audio.html
/usr/share/doc/xpra/Subsystems/Clipboard.html
/usr/share/doc/xpra/Subsystems/Logging.html
/usr/share/doc/xpra/Subsystems/MMAP.html
/usr/share/doc/xpra/Subsystems/Notifications.html
/usr/share/doc/xpra/Subsystems/Webcam.html
/usr/share/doc/xpra/Subsystems/index.html
/usr/share/doc/xpra/Usage/Apache-Proxy.html
/usr/share/doc/xpra/Usage/Authentication.html
/usr/share/doc/xpra/Usage/Client-OpenGL.html
/usr/share/doc/xpra/Usage/Client.html
/usr/share/doc/xpra/Usage/Configuration.html
/usr/share/doc/xpra/Usage/Desktop.html
/usr/share/doc/xpra/Usage/Encodings.html
/usr/share/doc/xpra/Usage/Logging.html
/usr/share/doc/xpra/Usage/NVENC.html
/usr/share/doc/xpra/Usage/OpenGL.html
/usr/share/doc/xpra/Usage/Proxy-Server.html
/usr/share/doc/xpra/Usage/Seamless.html
/usr/share/doc/xpra/Usage/Security.html
/usr/share/doc/xpra/Usage/Service.html
/usr/share/doc/xpra/Usage/Shadow.html
/usr/share/doc/xpra/Usage/WSL.html
/usr/share/doc/xpra/Usage/Xdummy.html
/usr/share/doc/xpra/Usage/index.html
/usr/share/doc/xpra/images/Xpra-Proxy.png
/usr/share/doc/xpra/images/icons/X11.png
/usr/share/doc/xpra/images/icons/authentication.png
/usr/share/doc/xpra/images/icons/clipboard.png
/usr/share/doc/xpra/images/icons/connect.png
/usr/share/doc/xpra/images/icons/debian.png
/usr/share/doc/xpra/images/icons/encoding.png
/usr/share/doc/xpra/images/icons/freebsd.png
/usr/share/doc/xpra/images/icons/keyboard.png
/usr/share/doc/xpra/images/icons/mdns.png
/usr/share/doc/xpra/images/icons/nvidia.png
/usr/share/doc/xpra/images/icons/opengl.png
/usr/share/doc/xpra/images/icons/osx.png
/usr/share/doc/xpra/images/icons/package.png
/usr/share/doc/xpra/images/icons/printer.png
/usr/share/doc/xpra/images/icons/quic.png
/usr/share/doc/xpra/images/icons/rpm.png
/usr/share/doc/xpra/images/icons/server-connected.png
/usr/share/doc/xpra/images/icons/sound.png
/usr/share/doc/xpra/images/icons/ssh.png
/usr/share/doc/xpra/images/icons/ubuntu.png
/usr/share/doc/xpra/images/icons/upload.png
/usr/share/doc/xpra/images/icons/webcam.png
/usr/share/doc/xpra/images/icons/windows.png
/usr/share/doc/xpra/images/logos/atos-black.png
/usr/share/doc/xpra/images/logos/corning.png
/usr/share/doc/xpra/images/logos/vpo-small.png
/usr/share/doc/xpra/images/mdns-gui.png
/usr/share/doc/xpra/images/pavucontrol-client.png
/usr/share/doc/xpra/images/pavucontrol-server.png
/usr/share/doc/xpra/images/screenshots/gnome-shell-notification.png
/usr/share/doc/xpra/images/screenshots/osx-notification.png
/usr/share/doc/xpra/images/screenshots/win11-glxspheres.png
/usr/share/doc/xpra/images/screenshots/win32-notification.png
/usr/share/doc/xpra/images/screenshots/win32-shadow-tray-menu.png
/usr/share/doc/xpra/images/session-info-graphs.png
/usr/share/doc/xpra/images/session-info-sound.png
/usr/share/doc/xpra/images/upload.png
/usr/share/doc/xpra/images/win32-shadow-tray-menu.png
/usr/share/doc/xpra/index.html

%files libexec
%defattr(-,root,root,-)
/usr/libexec/xpra/auth_dialog
/usr/libexec/xpra/gnome-open
/usr/libexec/xpra/gvfs-open
/usr/libexec/xpra/xdg-open
/usr/libexec/xpra/xpra_signal_listener
/usr/libexec/xpra/xpra_udev_product_version

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-xpra/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/pypi-xpra/c722dc46afe54071fb7d5c3f48ef46f4b54cafee
/usr/share/package-licenses/pypi-xpra/f45ee1c765646813b442ca58de72e20a64a7ddba

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/run_scaled.1
/usr/share/man/man1/xpra.1
/usr/share/man/man1/xpra_launcher.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
