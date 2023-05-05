Name: tint3
Summary: A C++ rewrite of the tint2 panel
Version: 0.3.0
Release: 9.1
Group: X Desktop
License: GPL2
URL: https://github.com/jmc-88/tint3
Source0: %{name}-master.zip
BuildRequires:  imlib2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libasan
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libX11-devel
BuildRequires:  pango-devel
BuildRequires:  librsvg2-devel
BuildRequires:  startup-notification-devel
BuildRequires:  pandoc
BuildRequires:  cmake

%description
This project aims to continue the development of tint2, port it to C++,
make it safer against crashes, and have it use XCB instead of Xlib.

%prep
%setup -q -n %{name}-master
sed -i -e 's|X11 Xcomposite|Xcomposite|' -e 's|Xrandr>=1.3|Xrandr|' CMakeLists.txt
sed -i '112,115d' src/theme_manager.cc
%ifarch aarch64
sed -i 's|SIGSTKSZ|8192|' external_includes/catch.hpp
%endif

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build -j1

%install
%cmake_install

%files
%{_sysconfdir}/xdg
%{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man?/*
%{_datadir}/%{name}

%changelog
* Sun Apr 9 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0
- Rebuilt for Fedora
* Sun Jul 04 2010 Eric Noulard <eric.noulard@gmail.com> - 0.3.0-1
- Generated by CPack RPM (no Changelog file were provided)
