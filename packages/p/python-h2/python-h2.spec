#
# spec file for package python-h2
#
# Copyright (c) 2020 SUSE LLC
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
%bcond_without python2
Name:           python-h2
Version:        3.2.0
Release:        0
Summary:        HTTP/2 State-Machine based protocol implementation
License:        MIT
URL:            https://github.com/python-hyper/hyper-h2
Source0:        https://files.pythonhosted.org/packages/source/h/h2/h2-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/python-hyper/hyper-h2/commit/c5d962a14373acf534be620d4e597dfeaff8a2ef bump hyperframe and fix protocol error
Patch0:         hyperframe.patch
BuildRequires:  %{python_module hpack >= 2.3}
BuildRequires:  %{python_module hyperframe >= 6.0}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-hpack >= 2.3
Requires:       python-hyperframe >= 6.0
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-enum34 >= 1.1.6
%endif
%ifpython2
Requires:       python-enum34 >= 1.1.6
%endif
%python_subpackages

%description
Pure-Python implementation of a HTTP/2 protocol stack.
It’s written from the ground up to be embeddable in whatever program
you choose to use, ensuring that you can speak HTTP/2 regardless of
your programming paradigm.

%prep
%setup -q -n h2-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_changing_max_frame_size - flaky in OBS
# test_range_of_acceptable_outputs -flaky in OBS
%pytest -k 'not (test_changing_max_frame_size or test_range_of_acceptable_outputs)'

%files %{python_files}
%license LICENSE
%doc HISTORY.rst README.rst
%{python_sitelib}/h2
%{python_sitelib}/h2-%{version}-py*.egg-info

%changelog
