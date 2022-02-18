#
# spec file for package python-pycups
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python3-%{**}}
%global skip_python2 1
Name:           python-pycups
Version:        2.0.1
Release:        0
Summary:        Python Bindings for CUPS
License:        GPL-2.0-or-later
Group:          Development/Libraries/Python
URL:            https://github.com/OpenPrinting/pycups
Source:         https://files.pythonhosted.org/packages/source/p/pycups/pycups-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  cups-devel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# need to avoid cycle as cups-devel wants us (boo#1172407)
#!BuildIgnore:  cups-rpm-helper
Obsoletes:      python-cups < %{version}
Provides:       python-cups = %{version}
%python_subpackages

%description
Python Bindings for CUPS, the Common Unix Printing System

%package -n cups-rpm-helper
Summary:        RPM macros for building cups drivers
Group:          Development/Libraries/Python
URL:            https://fedoraproject.org/wiki/Features/AutomaticPrintDriverInstallation
Requires:       python3-cups
Requires:       rpm-build
Supplements:    (rpm-build and cups-devel)

%description -n cups-rpm-helper
RPM helper scripts to create automatic "Provides:" tags for printer
driver RPMs.

%prep
%setup -q -n pycups-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
make install-rpmhook DESTDIR=%{buildroot}

%files %{python_files}
%doc NEWS README TODO
%license COPYING
%{python_sitearch}/cups*.so
%{python_sitearch}/pycups-%{version}-py*.egg-info

%files -n cups-rpm-helper
%{_rpmconfigdir}/fileattrs/psdriver.attr
%{_rpmconfigdir}/postscriptdriver.prov

%changelog
