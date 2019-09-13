#
# spec file for package python-cssutils
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define oldpython python
Name:           python-cssutils
Version:        1.0.2
Release:        0
Summary:        A CSS Cascading Style Sheets library for Python
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://cthedot.de/cssutils/
Source:         https://files.pythonhosted.org/packages/source/c/cssutils/cssutils-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-css-utils-doc = %{version}
Obsoletes:      %{oldpython}-css-utils-doc < %{version}
%endif
%python_subpackages

%description
A Python package to parse and build CSS Cascading Style Sheets. DOM only, not any rendering facilities!

%prep
%setup -q -n cssutils-%{version}
sed -i "1d" src/cssutils/{parse,codec,sac,serialize,scripts/csscapture,_codec2,errorhandler,scripts/cssparse,_codec3,scripts/csscombine,tokenize2,__init__}.py # Fix non-executable scripts
sed -i "s/\r//" src/cssutils/{sac,scripts/csscombine,tokenize2}.py COPYING COPYING.LESSER examples/{website,minify,imports,cssencodings,style,testutil,codec}.py # Fix EOL encodings

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/csscapture
%python_clone -a %{buildroot}%{_bindir}/csscombine
%python_clone -a %{buildroot}%{_bindir}/cssparse

%post
%{python_install_alternative csscapture csscombine cssparse}

%postun
%python_uninstall_alternative csscapture

%files %{python_files}
%license COPYING COPYING.LESSER
%doc README.txt examples
%python_alternative %{_bindir}/csscapture
%python_alternative %{_bindir}/csscombine
%python_alternative %{_bindir}/cssparse
%{python_sitelib}/cssutils-%{version}-py*.egg-info/
%{python_sitelib}/cssutils/
%{python_sitelib}/encutils/

%changelog
