Name:           gstreamer-plugins-tis
Version:        0.1
Release:        4.1
Summary:        Additional resources to control your TIS camera
License:        Apache License 2.0
URL:            https://github.com/TheImagingSource/tiscamera
Source0:        tiscamera-master.zip
BuildRequires:  gstreamer-devel       
BuildRequires:  libaravis-devel
BuildRequires:  systemd-devel

%description
* gstreamer elements
* uvc extensions
* firmware update tools
* examples on how to interact with your camera

%prep
%setup -q -n tiscamera-master
sed -i 's|PLUGIN_INSTALL_DIR=.*|PLUGIN_INSTALL_DIR=$(DESTDIR)%{_libdir}/gstreamer-0.10|' src/Makefile.in

%build
export LDFLAGS=-I/usr/include/aravis-0.4
cd src
./bootstrap.sh
%configure
make %{?_smp_mflags}

%install
cd src
%make_install

%files
%doc LICENSE README.md
%{_libdir}/gstreamer-0.10/libgsttis*.so

%changelog
* Wed Feb 25 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuild for Fedora
