#
# spec file for package httperf
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           httperf
Version:        0.9.0+git.20180712
Release:        0
Summary:        A tool for measuring web server performance
License:        SUSE-GPL-2.0+-with-openssl-exception
Group:          Productivity/Networking/Web/Utilities
Url:            https://github.com/httperf/httperf
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.changes
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)

%description
httperf is a tool for measuring web server performance. It provides a
flexible facility for generating various HTTP workloads and for measuring
server performance.

%prep
%setup -q
if [ -z "$SOURCE_DATE_EPOCH" ]; then
# replace build date with date from changelog
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE1}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find .  -name '*.[ch]' |\
    xargs sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g"
fi
chmod -x AUTHORS ChangeLog NEWS README.md TODO

%build
mkdir m4
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc AUTHORS ChangeLog NEWS README.md TODO
%{_bindir}/httperf
%{_mandir}/man1/httperf.1%{ext_man}
%{_mandir}/man1/idleconn.1%{ext_man}

%changelog
