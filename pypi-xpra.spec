#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-xpra
Version  : 4.4.1
Release  : 32
URL      : https://files.pythonhosted.org/packages/7c/47/e1d1238e7490534314e6ad66a5d4dbe3e3c051bb9081a1d71f181ee42c51/xpra-4.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/7c/47/e1d1238e7490534314e6ad66a5d4dbe3e3c051bb9081a1d71f181ee42c51/xpra-4.4.1.tar.gz
Summary  : runs X clients, typically on a remote host, and directs their display to the local machine without losing any state.
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 GPL-2.0+ GPL-3.0 GPL-3.0+ LGPL-2.0 LGPL-3.0 LGPL-3.0+ MIT MPL-1.1 Python-2.0
Requires: pypi-xpra-bin = %{version}-%{release}
Requires: pypi-xpra-config = %{version}-%{release}
Requires: pypi-xpra-data = %{version}-%{release}
Requires: pypi-xpra-filemap = %{version}-%{release}
Requires: pypi-xpra-lib = %{version}-%{release}
Requires: pypi-xpra-libexec = %{version}-%{release}
Requires: pypi-xpra-license = %{version}-%{release}
Requires: pypi-xpra-man = %{version}-%{release}
Requires: pypi-xpra-python = %{version}-%{release}
Requires: pypi-xpra-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pandoc
BuildRequires : pkgconfig(gdk-3.0)
BuildRequires : pkgconfig(liblz4)
BuildRequires : pkgconfig(py3cairo)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xres)
BuildRequires : pkgconfig(xtst)
BuildRequires : pypi(cython)

%description
Xpra gives you "persistent remote applications" for X. That is, unlike normal X applications, applications run with xpra are "persistent" -- you can run them remotely, and they don't die if your connection does. You can detach them, and reattach them later -- even from another computer -- with no loss of state. And unlike VNC or RDP, xpra is for remote applications, not remote desktops -- individual applications show up as individual windows on your screen, managed by your window manager. They're not trapped in a box.

So basically it's screen for remote X apps.

This metapackage installs the python3 version of xpra in full, including the python client, server and HTML5 client.

%package bin
Summary: bin components for the pypi-xpra package.
Group: Binaries
Requires: pypi-xpra-data = %{version}-%{release}
Requires: pypi-xpra-libexec = %{version}-%{release}
Requires: pypi-xpra-config = %{version}-%{release}
Requires: pypi-xpra-license = %{version}-%{release}
Requires: pypi-xpra-filemap = %{version}-%{release}

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


%package filemap
Summary: filemap components for the pypi-xpra package.
Group: Default

%description filemap
filemap components for the pypi-xpra package.


%package lib
Summary: lib components for the pypi-xpra package.
Group: Libraries
Requires: pypi-xpra-data = %{version}-%{release}
Requires: pypi-xpra-libexec = %{version}-%{release}
Requires: pypi-xpra-license = %{version}-%{release}
Requires: pypi-xpra-filemap = %{version}-%{release}

%description lib
lib components for the pypi-xpra package.


%package libexec
Summary: libexec components for the pypi-xpra package.
Group: Default
Requires: pypi-xpra-config = %{version}-%{release}
Requires: pypi-xpra-license = %{version}-%{release}
Requires: pypi-xpra-filemap = %{version}-%{release}

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
Requires: pypi-xpra-filemap = %{version}-%{release}
Requires: python3-core

%description python3
python3 components for the pypi-xpra package.


%prep
%setup -q -n xpra-4.4.1
cd %{_builddir}/xpra-4.4.1
pushd ..
cp -a xpra-4.4.1 buildavx2
popd

%build
## build_prepend content
export CPPFLAGS="${CPPFLAGS} -I/usr/include"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666365609
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build  %{?_smp_mflags}

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build  %{?_smp_mflags}

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-xpra
cp %{_builddir}/xpra-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-xpra/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/xpra-%{version}/xpra/gtk_common/gtk2_notifier-LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-xpra/f45ee1c765646813b442ca58de72e20a64a7ddba || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib/sysusers.d/xpra.conf
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
/usr/share/xpra/cuda/README.md
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

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/xpra/Build/Debian.html
/usr/share/doc/xpra/Build/Dependencies.html
/usr/share/doc/xpra/Build/MSWindows.html
/usr/share/doc/xpra/Build/MacOS.html
/usr/share/doc/xpra/Build/Other.html
/usr/share/doc/xpra/Build/RPM.html
/usr/share/doc/xpra/Build/index.html
/usr/share/doc/xpra/CHANGELOG.html
/usr/share/doc/xpra/FAQ.html
/usr/share/doc/xpra/Features/Audio.html
/usr/share/doc/xpra/Features/Clipboard.html
/usr/share/doc/xpra/Features/DPI.html
/usr/share/doc/xpra/Features/Display.html
/usr/share/doc/xpra/Features/File-Transfers.html
/usr/share/doc/xpra/Features/Image-Depth.html
/usr/share/doc/xpra/Features/Keyboard.html
/usr/share/doc/xpra/Features/Notifications.html
/usr/share/doc/xpra/Features/Printing.html
/usr/share/doc/xpra/Features/System-Tray.html
/usr/share/doc/xpra/Features/Webcam.html
/usr/share/doc/xpra/Features/index.html
/usr/share/doc/xpra/Network/AES.html
/usr/share/doc/xpra/Network/Encryption.html
/usr/share/doc/xpra/Network/Multicast-DNS.html
/usr/share/doc/xpra/Network/SSH.html
/usr/share/doc/xpra/Network/SSL.html
/usr/share/doc/xpra/Network/index.html
/usr/share/doc/xpra/Usage/Apache-Proxy.html
/usr/share/doc/xpra/Usage/Authentication.html
/usr/share/doc/xpra/Usage/Client-OpenGL.html
/usr/share/doc/xpra/Usage/Client.html
/usr/share/doc/xpra/Usage/Configuration.html
/usr/share/doc/xpra/Usage/Encodings.html
/usr/share/doc/xpra/Usage/Logging.html
/usr/share/doc/xpra/Usage/NVENC.html
/usr/share/doc/xpra/Usage/OpenGL.html
/usr/share/doc/xpra/Usage/Proxy-Server.html
/usr/share/doc/xpra/Usage/Seamless.html
/usr/share/doc/xpra/Usage/Security.html
/usr/share/doc/xpra/Usage/Service.html
/usr/share/doc/xpra/Usage/Shadow-Server.html
/usr/share/doc/xpra/Usage/Start-Desktop.html
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
/usr/share/doc/xpra/images/icons/rpm.png
/usr/share/doc/xpra/images/icons/server-connected.png
/usr/share/doc/xpra/images/icons/sound.png
/usr/share/doc/xpra/images/icons/ssh.png
/usr/share/doc/xpra/images/icons/ubuntu.png
/usr/share/doc/xpra/images/icons/upload.png
/usr/share/doc/xpra/images/icons/webcam.png
/usr/share/doc/xpra/images/icons/windows.png
/usr/share/doc/xpra/images/mdns-gui.png
/usr/share/doc/xpra/images/pavucontrol-client.png
/usr/share/doc/xpra/images/pavucontrol-server.png
/usr/share/doc/xpra/images/session-info-graphs.png
/usr/share/doc/xpra/images/session-info-sound.png
/usr/share/doc/xpra/images/upload.png
/usr/share/doc/xpra/images/win32-shadow-tray-menu.png
/usr/share/doc/xpra/index.html

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-xpra

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

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
/usr/lib/python3*/*
