#
# spec file for package python-traits
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define         oldpython python
Name:           python-traits
Version:        5.1.2
Release:        0
Summary:        Explicitly typed attributes for Python
# Images have different licenses. For image license breakdown check
# image_LICENSE.txt file. Except enthought/traits/ui/editors_gen.py
# which is GPLv2+ all remaining source or image files are in BSD
# 3-clause license. Confirmed from upstream.
License:        BSD-3-Clause AND EPL-1.0 AND LGPL-2.1-only
Group:          Development/Libraries/Python
Url:            https://github.com/enthought/traits
Source:         https://files.pythonhosted.org/packages/source/t/traits/traits-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
# /SECTION
Requires:       python-numpy
Requires:       python-six
Recommends:     python-traitsui
%ifpython2
Provides:       %{oldpython}-Traits = %{version}
Obsoletes:      %{oldpython}-Traits < %{version}
%endif

%python_subpackages

%description
The traits package developed by Enthought provides a special type definition
called a trait. Although they can be used as normal Python object attributes,
traits also have several additional characteristics:

 * Initialization: A trait can be assigned a default value.
 * Validation: A trait attribute's type can be explicitly declared.
 * Delegation: The value of a trait attribute can be contained either
   in another object.
 * Notification: Setting the value of a trait attribute can trigger
   notification of other parts of the program.
 * Visualization: User interfaces that permit the interactive
   modification of a trait's value can be automatically constructed
   using the trait's definition.

Part of the Enthought Tool Suite (ETS).

%prep
%setup -q -n traits-%{version}
%fdupes examples/
# file not utf-8
iconv -f iso8859-1 -t utf-8 image_LICENSE_Eclipse.txt > image_LICENSE_Eclipse.txt.conv
mv -f image_LICENSE_Eclipse.txt.conv image_LICENSE_Eclipse.txt

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%{python_expand mkdir tester_%{$python_bin_suffix}
pushd tester_%{$python_bin_suffix}
export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -m nose.core -v traits
popd
}

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGES.rst README.rst
%doc examples/
%license LICENSE.txt image_LICENSE*.txt
%{python_sitearch}/traits/
%{python_sitearch}/traits-%{version}-py*.egg-info

%changelog
