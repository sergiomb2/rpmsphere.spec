Name:           azpainter
Version:        2.1.5
Release:        1
Summary:        Painting software
License:        GPL3.0+
Group:          Productivity/Graphics/Other
URL:            https://osdn.net/projects/azpainter
Source:         https://osdn.net/projects/azpainter/downloads/71988/%{name}-%{version}.tar.xz
BuildRequires:  automake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  desktop-file-utils

%description
Full color painting software for Linux for illustration drawing.
This is not suitable for dot editing.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%post
%{_bindir}/update-desktop-database --quiet "%{_datadir}/applications" || :
%{_bindir}/update-mime-database -n "%{_datadir}/mime" || :

%postun
%{_bindir}/update-desktop-database --quiet "%{_datadir}/applications" || :
%{_bindir}/update-mime-database -n "%{_datadir}/mime" || :

%files
%doc AUTHORS ChangeLog NEWS README README_ja
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*%{name}*.??g
%{_datadir}/mime/packages/%{name}.xml
%license COPYING GPL3

%changelog
* Mon Dec 09 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.5
- Rebuild for Fedora
