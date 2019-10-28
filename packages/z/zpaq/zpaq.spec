#
# spec file for package zpaq
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define         dversion 715
Name:           zpaq
Version:        7.15
Release:        0
Summary:        A journaling, incremental, deduplicating archiver
License:        SUSE-Public-Domain AND MIT
Group:          Productivity/Archiving/Compression
Url:            http://mattmahoney.net/dc/zpaq.html
Source0:        http://mattmahoney.net/dc/zpaq%{dversion}.zip
Source1:        %{name}.changes
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  unzip

%description
zpaq is a journaling, incremental, deduplicating archiver.
"Journaling" means that when you update a file or directory, both the
old and new versions are saved and can be extracted. "Incremental"
means that only those files whose last-modified date has changed
since the previous backup are added. For 100 GB of files, this
typically takes 1-2 minutes, vs. a few hours to create the first
version. "Deduplicating" means that identical files or fragments are
stored only once to save time and space.

%prep
%setup -q -c %{name}%{dversion}
dos2unix readme.txt COPYING
# remove date and time from binary
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE1}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find .  -name '*.cpp' |\
    xargs sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g"

%build
make %{?_smp_mflags} CXXFLAGS="%{optflags}"

%install
make \
  install \
  DESTDIR="%{?buildroot}" \
  LIBDIR="%{_libdir}" \
  BINDIR="%{_bindir}" \
  MANDIR="%{_mandir}" \
  INCLUDEDIR="%{_includedir}" \

%files
%doc readme.txt
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
