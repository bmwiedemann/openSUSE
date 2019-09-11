#
# spec file for package python-rcssmin
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}

%define mod_name rcssmin

Name:           python-%{mod_name}
Version:        1.0.6
Release:        0
Summary:        RCSSmin is a CSS Minifier Written in Python
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            http://opensource.perlig.de/rcssmin/
Source:         https://files.pythonhosted.org/packages/source/r/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%python_subpackages

%description
rCSSmin is a CSS minifier written in python.

The minifier is based on the semantics of the YUI compressor, which
itself is based on the rule list by Isaac Schlueter.

This module is a re-implementation aiming for speed instead of maximum
compression, so it can be used at runtime (rather than during a
preprocessing step). rCSSmin does syntactical compression only
(removing spaces, comments and possibly semicolons). It does not
provide semantic compression (like removing empty blocks, collapsing
redundant properties etc). It does, however, support various CSS hacks
(by keeping them working as intended).

%package -n %{name}-docs
Summary:        Documentation files for %name
Group:          Documentation/HTML

%description -n %{name}-docs
HTML Documentation and examples for %name.

%prep
%setup -q -n %{mod_name}-%{version}

%build
%python_build

%install
%python_install
rm -rf %{buildroot}/usr/share/doc/rcssmin

%files %{python_files}
%defattr(-,root,root,-)
%doc LICENSE README.rst docs/CHANGES
%{python_sitearch}/*

%files -n %{name}-docs
%doc docs/apidoc/

%changelog
