#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xpra
Version  : 4.2.3
Release  : 20
URL      : https://files.pythonhosted.org/packages/7f/12/0657446d77fdea4041a748a8df6e05ee41c43a8c6f1ca20082c38f6dc84d/xpra-4.2.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/7f/12/0657446d77fdea4041a748a8df6e05ee41c43a8c6f1ca20082c38f6dc84d/xpra-4.2.3.tar.gz
Summary  : runs X clients, typically on a remote host, and directs their display to the local machine without losing any state.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GPL-2.0 GPL-2.0+ GPL-3.0 GPL-3.0+ LGPL-2.0 LGPL-3.0 LGPL-3.0+ MIT MPL-1.1
Requires: xpra-bin = %{version}-%{release}
Requires: xpra-config = %{version}-%{release}
Requires: xpra-data = %{version}-%{release}
Requires: xpra-license = %{version}-%{release}
Requires: xpra-man = %{version}-%{release}
Requires: xpra-python = %{version}-%{release}
Requires: xpra-python3 = %{version}-%{release}
Requires: xpra-services = %{version}-%{release}
BuildRequires : Cython
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-gnome
BuildRequires : pandoc
BuildRequires : pkgconfig(gdk-3.0)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : pkgconfig(py3cairo)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xtst)
BuildRequires : pycairo-dev
BuildRequires : pygobject
BuildRequires : python3-dev

%description
Yasm is a complete rewrite of the NASM assembler under the "new" BSD License
(some portions are under other licenses, see COPYING for details). It is
designed from the ground up to allow for multiple assembler syntaxes to be
supported (eg, NASM, TASM, GAS, etc.) in addition to multiple output object
formats and even multiple instruction sets. Another primary module of the
overall design is an optimizer module.

%package bin
Summary: bin components for the xpra package.
Group: Binaries
Requires: xpra-data = %{version}-%{release}
Requires: xpra-config = %{version}-%{release}
Requires: xpra-license = %{version}-%{release}
Requires: xpra-services = %{version}-%{release}

%description bin
bin components for the xpra package.


%package config
Summary: config components for the xpra package.
Group: Default

%description config
config components for the xpra package.


%package data
Summary: data components for the xpra package.
Group: Data

%description data
data components for the xpra package.


%package doc
Summary: doc components for the xpra package.
Group: Documentation
Requires: xpra-man = %{version}-%{release}

%description doc
doc components for the xpra package.


%package license
Summary: license components for the xpra package.
Group: Default

%description license
license components for the xpra package.


%package man
Summary: man components for the xpra package.
Group: Default

%description man
man components for the xpra package.


%package python
Summary: python components for the xpra package.
Group: Default
Requires: xpra-python3 = %{version}-%{release}

%description python
python components for the xpra package.


%package python3
Summary: python3 components for the xpra package.
Group: Default
Requires: python3-core

%description python3
python3 components for the xpra package.


%package services
Summary: services components for the xpra package.
Group: Systemd services

%description services
services components for the xpra package.


%prep
%setup -q -n xpra-4.2.3
cd %{_builddir}/xpra-4.2.3

%build
## build_prepend content
export CPPFLAGS="${CPPFLAGS} -I/usr/include"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636482459
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xpra
cp %{_builddir}/xpra-4.2.3/COPYING %{buildroot}/usr/share/package-licenses/xpra/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/xpra-4.2.3/xpra/gtk_common/gtk2_notifier-LICENSE.txt %{buildroot}/usr/share/package-licenses/xpra/f45ee1c765646813b442ca58de72e20a64a7ddba
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}*/usr/lib/sysusers.d/xpra.conf

%files
%defattr(-,root,root,-)
/usr/lib/cups/backend/xpraforwarder
/usr/lib/xpra/auth_dialog
/usr/lib/xpra/gnome-open
/usr/lib/xpra/gvfs-open
/usr/lib/xpra/xdg-open

%files bin
%defattr(-,root,root,-)
/usr/bin/run_scaled
/usr/bin/xpra
/usr/bin/xpra_Xdummy
/usr/bin/xpra_launcher
/usr/bin/xpra_signal_listener
/usr/bin/xpra_udev_product_version

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
/usr/share/xpra/icons/download.png
/usr/share/xpra/icons/empty.png
/usr/share/xpra/icons/encoding.png
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
%doc /usr/share/doc/xpra/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xpra/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/xpra/f45ee1c765646813b442ca58de72e20a64a7ddba

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

%files services
%defattr(-,root,root,-)
/lib/systemd/system/xpra.service
/lib/systemd/system/xpra.socket
