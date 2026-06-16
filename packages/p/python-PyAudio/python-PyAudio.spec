#
# spec file for package python-PyAudio
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_without  test
Name:           python-PyAudio
Version:        0.2.14
Release:        0
Summary:        Python Bindings for PortAudio v19
License:        MIT
URL:            https://people.csail.mit.edu/hubert/pyaudio/
Source:         https://files.pythonhosted.org/packages/source/P/PyAudio/PyAudio-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with test}
%check
# skip tests requiring hardware
export PYAUDIO_SKIP_HW_TESTS=1
# rise up segmentation fault
rm tests/error_tests.py
rm tests/misc_tests.py
%pyunittest_arch discover -p '*.py' -v -s tests
%endif

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG README.md
%doc examples/
%{python_sitearch}/pyaudio/_portaudio*.so
%{python_sitearch}/pyaudio/
%{python_sitearch}/[Pp]y[Aa]udio-%{version}.dist-info

%changelog
