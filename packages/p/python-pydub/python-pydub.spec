#
# spec file for package python-pydub
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


%if 0%{?!ffmpeg_pref:1}
%if 0%{?suse_version} >= 1550
%define ffmpeg_pref ffmpeg-6
%else
%define ffmpeg_pref ffmpeg-4
%endif
%endif

%{?sle15_python_module_pythons}
Name:           python-pydub
Version:        0.25.1
Release:        0
Summary:        Audio manipulation with Python
License:        MIT
URL:            https://github.com/jiaaro/pydub
Source:         https://github.com/jiaaro/pydub/archive/v%{version}.tar.gz#/pydub-%{version}.tar.gz
# PATCH-FIX-OPENSUSE skip_libopenh264-7.patch gh#jiaaro/pydub#700 mcepl@suse.com
# We don't have libopenh264-7 on the plain openSUSE
Patch0:         skip_libopenh264-7.patch
# PATCH-FIX-UPSTREAM gh#jiaaro/pydub#769
Patch1:         fix-assertions.patch
BuildRequires:  %{ffmpeg_pref}
BuildRequires:  %{python_module audioop-lts if %python-base >= 3.13}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildConflicts: %{ffmpeg_pref}-mini-libs
BuildRequires:  python-rpm-macros
Requires:       %{ffmpeg_pref}
%if 0%{?python_version_nodots} >= 313
Requires:       python-audioop-lts
%endif
Recommends:     python-scipy
Recommends:     python-simpleaudio
BuildArch:      noarch
%python_subpackages

%description
A Python module to manipulate audio with a high level interface.

%prep
%autosetup -p1 -n pydub-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export NO_OPENH264=1
%pytest test/test.py

%files %{python_files}
%license LICENSE
%{python_sitelib}/pydub-%{version}.dist-info
%{python_sitelib}/pydub

%changelog
