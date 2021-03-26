%global theme	Numix-Circle

Name:		numix-icon-theme-circle
Version:	14.10.2
Release:	3.1
Summary:	%{theme} icon theme
Group:		System/Configuration/Theme
License:	GPL-3
URL:		http://www.numixproject.org
Source0:	%{name}-master.tar.xz
BuildArch:	noarch

%description
%{theme} is an icon theme from the Numix project.

%prep
%setup -q -n %{name}-master

%build

%install
rm -rf %{buildroot}
%{__install} -d -m755 %{buildroot}%{_datadir}/icons/
%{__cp} -pr %{theme} %{buildroot}%{_datadir}/icons/

%clean
%__rm -rf "%{buildroot}"

%files
%{_datadir}/icons/%{theme}

%changelog
* Wed Jul 08 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 14.10.2
- Rebuild for Fedora
* Thu Oct 30 2014 Agent Smith <ruidobranco@yahoo.com.br> 14.10.2-1pclos2014
- Created package numix-icon-theme
