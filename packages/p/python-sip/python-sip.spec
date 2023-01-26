#
# spec file for package python-sip
#
# Copyright (c) 2021 SUSE LLC
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


# Default is sip6 for all distributions. Be sure to branch both python-sip6 and python-sip into
# any project using this metapackge.
%define sipN sip6
# Assume that all installed python flavors have the same version
%define Nversion %(rpm -q --qf '%%{version}' --whatprovides $(echo %{python_module %{sipN}-devel}| cut -d " " -f 1))
%define skip_python2 1
%define plainpython python
Name:           python-sip
Version:        %{Nversion}
Release:        0
Summary:        A Python bindings generator for C/C++ libraries
License:        GPL-2.0-only OR GPL-3.0-only OR SUSE-SIP
Group:          Development/Libraries/Python
URL:            https://www.riverbankcomputing.com/software/sip
Source0:        README.SUSE
BuildRequires:  %{python_module %{sipN}-devel}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%requires_eq    python-%{sipN}
%python_subpackages

%description
SIP is a collection of tools that makes it very easy to create Python
bindings for C and C++ libraries. It was originally developed in 1998
to create PyQt, the Python bindings for the Qt toolkit, but can be used
to create bindings for any C or C++ library. For example it is also used
to generate wxPython, the Python bindings for wxWidgets.

%package devel
Summary:        A Python bindings generator for C/C++ libraries
Group:          Development/Libraries/Python
%requires_eq    python-%{sipN}-devel

%description devel
SIP is a collection of tools that makes it very easy to create Python
bindings for C and C++ libraries. It was originally developed in 1998
to create PyQt, the Python bindings for the Qt toolkit, but can be used
to create bindings for any C or C++ library. For example it is also used
to generate wxPython, the Python bindings for wxWidgets.

This package contains all the developer tools you need to create your
own sip bindings in the currently default version. Look for
%{python_prefix}-sip<N>-devel, if you need to build a package with a
specific version of SIP v<N>.

%package -n python-sip-doc
Summary:        A Python bindings generator for C/C++ libraries -- common documentation
Group:          Development/Libraries/Python
Provides:       %{python_module sip-doc = %{version}-%{release}}
%requires_eq    %{plainpython}-%{sipN}-doc

%description -n python-sip-doc
SIP is a tool that makes it very easy to create Python bindings for C
and C++ libraries. It was originally developed to create PyQt, the
Python bindings for the Qt toolkit, but can be used to create bindings
for any C or C++ library.

This package contains the documentation and example files in the
currently default version. Look for %{python_prefix}-sip<N>-devel, 
if you need to build a package with a specific version of SIP v<N>.

%prep
%setup -q -T -c
cp %{SOURCE0} .

%build
:

%install
:

%if "%{sipN}" == "sip4"
# only sip4 still provides the old python-sip package
%files %{python_files}
%doc README.SUSE
%endif

%files %{python_files devel}
%doc README.SUSE

%files -n python-sip-doc
%doc README.SUSE

%changelog
