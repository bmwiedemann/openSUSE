#
# spec file for package python-audioread
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-audioread
Version:        3.0.1
Release:        0
Summary:        Wrapper for audio decoding via selectable backends
License:        MIT
URL:            https://github.com/beetbox/audioread
Source0:        https://github.com/beetbox/audioread/archive/v%{version}.tar.gz
# PATCH-FIX-OPENSUSE Do not use rawread backend on Python 3.13+
Patch0:         no-removed-formats.patch
BuildRequires:  %{ffmpeg_pref}
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildConflicts: %{ffmpeg_pref}-mini-libs
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Recommends:     /usr/bin/ffmpeg
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
%autosetup -p1 -n audioread-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/audioread
%{python_sitelib}/audioread-%{version}.dist-info

%changelog
