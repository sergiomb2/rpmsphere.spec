Name: python-pyminuit
Summary: Minuit interface for minimizing Python functions
Version: 1.2.1
Release: 6.1
Group: Development/Libraries
License: GPL
URL: http://code.google.com/p/pyminuit/
Source0: http://pyminuit.googlecode.com/files/pyminuit-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python-devel
BuildRequires: minuit-devel

%description
PyMinuit is an extension module for Python that passes low-level Minuit
functionality to Python functions. Interaction and data exploration is more
user-friendly, in the sense that the user is protected from segmentation
faults and index errors, parameters are referenced by their names, even in
correlation matrices, and Python exceptions can be passed from the objective
function during the minimization process. This extension module also makes
it easier to calculate Minos errors and contour curves at an arbitrary number
of sigmas from the minimum, and features a new N-dimensional scanning utility.

%prep
%setup -q -n pyminuit

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%files
%doc COPYING AUTHORS
%{python_sitearch}/*

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.1
- Rebuild for Fedora
