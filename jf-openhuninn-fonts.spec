%define	_name	jf-openhuninn
%define fontdir %{_datadir}/fonts/%{_name}

Summary: Justfont OpenHuninn TrueType Fonts
Name: jf-openhuninn-fonts
Version: 1.1.a
Release: 1
License: OFL 1.1
Group: User Interface/X
URL: https://github.com/tasi788/open-huninn-font
BuildArch: noarch
Source0: jf-openhuninn-%{version}.zip
Requires: fontconfig

%description
JF Open Huninn is an opensource font based on Kosugi Maru (by Motoya) and
Varela Round (by Joe Prince and Avraham Cornfeld), then optimized by justfont
designers according to daily applications in Taiwan.

This is a fork of https://github.com/justfont/open-huninn-font
to remove version number in font-family-name.

%prep
%setup -q -n %{_name}-%{version}

%build

%install
install -d $RPM_BUILD_ROOT%{fontdir}
install -m644 *.ttf $RPM_BUILD_ROOT%{fontdir}

%post
fc-cache 2> /dev/null

%postun
fc-cache 2> /dev/null

%files
%doc license.txt README.md
%{fontdir}

%changelog
* Tue Apr 28 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.a
- Initial package
