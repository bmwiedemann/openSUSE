#
# spec file for package python-PyAudio
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without  test
Name:           python-PyAudio
Version:        0.2.11
Release:        0
Summary:        Python Bindings for PortAudio v19
License:        MIT
URL:            https://people.csail.mit.edu/hubert/pyaudio/
Source:         https://files.pythonhosted.org/packages/source/P/PyAudio/PyAudio-%{version}.tar.gz
# PATCH-FIX-UPSTREAM loopback_required.patch mcepl@suse.com
# Mark tests requiring specific hardware as such
Patch0:         loopback_required.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  portaudio-devel
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module numpy}
BuildRequires:  alsa
%endif
%python_subpackages

%description
PyAudio provides Python bindings for PortAudio v19, the cross-platform audio I/O library.
With PyAudio, you can easily use Python to play and record audio streams on a variety
of platforms (e.g., GNU/Linux, Microsoft Windows, and Mac OS X).

%prep
%setup -q -n PyAudio-%{version}
%autopatch -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with test}
%check
# report send to hubert@mit.edu
export HW_REQUIRED=1
%pyunittest_arch discover -p '*.py' -v -s tests
%endif

%files %{python_files}
%doc CHANGELOG README
%doc examples/
%{python_sitearch}/_portaudio*.so
%{python_sitearch}/pyaudio.py*
%pycache_only %{python_sitearch}/__pycache__/pyaudio*.py*
%{python_sitearch}/PyAudio-%{version}-py*.egg-info

%changelog
