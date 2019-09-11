#
# spec file for package python-audioread
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
Name:           python-audioread
Version:        2.1.8
Release:        0
Summary:        Wrapper for audio decoding via selectable backends
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/sampsyo/audioread
Source0:        https://github.com/beetbox/audioread/archive/v%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  ffmpeg
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Recommends:     ffmpeg
Recommends:     python-gobject
Recommends:     python-pymad
Recommends:     typelib(Gst) = 1.0

%python_subpackages

%description
Decode audio files using whichever backend is available. The library
currently supports:

- Gstreamer via PyGObject.
- MAD via the pymad bindings.
- FFmpeg or Libav via its command-line interface.
- The standard library wave, aifc, and sunau modules (for
  uncompressed audio formats).

%prep
%setup -q -n audioread-%{version}

%build
%python_build

%install
%python_install

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
