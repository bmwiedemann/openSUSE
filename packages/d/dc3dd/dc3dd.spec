#
# spec file for package dc3dd
#
# Copyright (c) 2025 SUSE LLC
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


Name:           dc3dd
Version:        7.3.1
Release:        0
Summary:        Patched dd with Computer Forensics Features
License:        GPL-3.0-only
Group:          Productivity/Archiving/Backup
URL:            https://sourceforge.net/projects/dc3dd/
Source0:        https://sourceforge.net/projects/dc3dd/files/dc3dd/%{version}/%{name}-%{version}.zip
# PATCH-FIX-UPSTREAMING -- bmwiedemann -- https://sourceforge.net/p/dc3dd/bugs/16/
Patch0:         reproducible.patch
# fix build with gcc15
Patch1:         dc3dd-gcc15.patch
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  unzip
BuildRequires:  perl(Locale::gettext)

%description
dc3dd is a patched version of GNU dd to include a number of features useful
for computer forensics. Many of these features were inspired by dcfldd, but
were rewritten for dc3dd.

* Pattern writes. The program can write a single hexadecimal value or a text
  string to the output device for wiping purposes.
* Piecewise and overall hashing with multiple algorithms and variable size
  windows. Supports MD5, SHA-1, SHA-256, and SHA-512. Hashes can be computed
  before or after conversions are made.
* Progress meter with automatic input/output file size probing
* Combined log for hashes and errors
* Error grouping. Produces one error message for identical sequential errors
* Verify mode. Able to repeat any transformations done to the input file and
  compare it to an output.
* Ability to split the output into chunks with numerical or alphabetic
  extensions

%lang_package

%prep
%autosetup -p1

# fix end-of-line encoding
sed -i 's/\r$//' *.txt
sed -i 's/\r$//' ChangeLog
# Add executable flag to configure
chmod +x build-aux/git-version-gen

%build
# hpa and dco detection is recommended for linux builds
autoreconf -fiv
%configure --enable-hpadco \
  gl_cv_func_printf_directive_n=yes \
  gl_cv_func_printf_infinite_long_double=yes
%make_build

%install
%make_install
%find_lang dc3dd

%files
%license COPYING
%doc ChangeLog NEWS THANKS
%doc *.txt
%{_bindir}/dc3dd
%{_mandir}/man1/dc3dd.1%{?ext_man}

%files lang -f %{name}.lang
%dir /usr/share/locale/*/LC_TIME

%changelog
