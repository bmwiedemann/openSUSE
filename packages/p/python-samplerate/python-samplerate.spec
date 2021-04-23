#
# spec file for package python-samplerate
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python36 1
%bcond_without  python2
Name:           python-samplerate
Version:        0.1.0
Release:        0
License:        MIT
Summary:        Python bindings for libsamplerate
URL:            https://github.com/tuxu/python-samplerate
Group:          Development/Languages/Python
Source0:        https://files.pythonhosted.org/packages/source/s/samplerate/samplerate-%{version}.tar.gz
Source1:        https://github.com/tuxu/python-samplerate/raw/%{version}/tests/test_samplerate.py
Source100:      python-samplerate-rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module cffi >= 1.0.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  libsamplerate
%if %{with python2}
BuildRequires:  python-enum34
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       libsamplerate
Requires:       python-cffi >= 1.0.0
Requires:       python-numpy
%ifpython2
Requires:       python-enum34
%endif
BuildArch:      noarch

%python_subpackages

%description
This is a wrapper around Erik de Castro Lopo's libsamplerate (aka Secret
Rabbit Code) for sample rate conversion.

It implements all three APIs available in libsamplerate:

* Simple API: for resampling a large chunk of data with a single library
  call
* Full API: for obtaining the resampled signal from successive chunks of
  data
* Callback API: like Full API, but input samples are provided by a callback
  function

%prep
%setup -q -n samplerate-%{version}
mkdir tests
cp %{SOURCE1} tests/
sed -i -e "s/, 'pytest-runner'//" -e "/tests_require/ d" setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Remove unneeded mac and windows library binaries
%python_expand rm %{buildroot}%{$python_sitelib}/samplerate/_samplerate_data/*.*

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.rst
%{python_sitelib}/samplerate
%{python_sitelib}/samplerate-%{version}*-info

%changelog
