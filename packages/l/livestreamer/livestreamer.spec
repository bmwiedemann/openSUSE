#
# spec file for package livestreamer
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           livestreamer
Version:        1.12.2
Release:        0
Summary:        Program to pipe streams from services into a video player
License:        BSD-2-Clause and MIT
Group:          Development/Languages/Python
Url:            http://livestreamer.io/
Source:         https://github.com/chrippa/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM livestreamer-use-mpv.patch sor.alexei@meowr.ru -- Use a lighter MPV player by default.
Patch0:         %{name}-use-mpv.patch
Recommends:     mpv
BuildArch:      noarch
%if 0%{?suse_version} > 1310
BuildRequires:  python3-devel >= 3.4
BuildRequires:  python3-setuptools
BuildRequires:  python3-Sphinx
Requires:       python3-requests >= 1.0
%else
BuildRequires:  python-devel >= 2.7
BuildRequires:  python-futures
BuildRequires:  python-setuptools
BuildRequires:  python-singledispatch
BuildRequires:  python-Sphinx
Requires:       python-requests >= 1.0
%endif

%description
Livestreamer is a command-line utility that pipes video streams
from various services into a video player, such as MPV. The main
purpose of Livestreamer is to allow the user to avoid buggy and
CPU heavy flash plugins but still be able to enjoy various streamed
content. There is also an API available for developers who want
access to the video stream data.

%prep
%setup -q
%patch0 -p1

%build
%if 0%{?suse_version} > 1310
python3 setup.py build
%else
python2 setup.py build
%endif

%install
%if 0%{?suse_version} > 1310
python3 setup.py install \
%else
python2 setup.py install \
%endif
  --root=%{buildroot} \
  --prefix=%{_prefix}

find %{buildroot}{%{python3_sitelib},%{python_sitelib}} -type f -name '*.py' | while read py; do
    if [[ "$(head -c2 "$py"; echo)" == "#!" ]]; then
        chmod a+x "$py"
    else
        chmod a-x "$py"
    fi
done

%files
%defattr(-,root,root)
%doc AUTHORS.rst CHANGELOG.rst CONTRIBUTING.rst LICENSE* MANIFEST.in README.rst
%{_bindir}/%{name}
%if 0%{?suse_version} > 1310
%{python3_sitelib}/%{name}*/
%else
%{python_sitelib}/%{name}*/
%endif

%changelog
