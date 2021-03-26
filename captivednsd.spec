%global debug_package %{nil}

Name:         captivednsd
Summary:      Captive DNS Server
URL:          http://www.aelius.com/njh/captivednsd/
Group:        DNS
License:      GPL
Version:      0.2
Release:      20081105.1
Source0:      http://www.aelius.com/njh/%{name}/%{name}-%{version}.tar.gz
Patch:       captivednsd.patch

%description
Captive Domain Name Server returns same authorative response to
every query. The reponse to 'A' queries and 'PTR' records are passed
as a parameter on the command line. It is intended to direct people
to a captive web portal, on a system that was not connected to the
Internet. This meant that it was not possible to resolve the correct
IP address for a host and then redirect the query using a firewall.

%prep
%setup -q
%patch -p0

%build
make %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuild for Fedora
