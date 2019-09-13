#
# spec file for package slrn
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


Name:           slrn
Version:        1.0.3
Release:        0
Summary:        Threaded Newsreader
License:        GPL-2.0-or-later
Group:          Productivity/Networking/News/Clients
URL:            http://www.slrn.org
Source:         %{name}-%{version}-gpl.tar.bz2
Source1:        clean-tar.sh
# PATCH-FIX-OPENSUSE slrn-do-not-strip-binaries.diff gber@opensuse.org -- Prevents binaris from being stripped
Patch0:         slrn-do-not-strip-binaries.patch
# PATCH-FIX-OPENSUSE slrn-correct-path-to-sendmail.patch sfalken@opensuse.org -- Replaces ed stanza in %%setup, it's failing, and I don't grok ed/regexp very well.
Patch2:         slrn-correct-path-to-sendmail.patch
BuildRequires:  mininews
BuildRequires:  pkgconfig
BuildRequires:  slang-devel
BuildRequires:  pkgconfig(libssl)
Recommends:     %{name}-lang = %{version}
# some slrn macros depend on certain slang modules
Recommends:     slang-slsh

%description
slrn is a threaded Internet newsreader. It is customizable,
permitting redefinition of keys and it includes a sophisticated macro
language for further customization.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch2 -p1

# replace __DATE__ and __TIME__ with date/time of the last specfile changelog
# entry
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find .  -name '*.[ch]' -print -exec sh -c '
    sed "/^[ \t]*#[ \t]*if/n;s/__DATE__/$3/g;s/__TIME__/$2/g" "$1" >"$1.new" && \
        mv "$1.new" "$1"
' {} {} "${TIME}" "${DATE}" \;

%build
%configure \
    --with-slrnpull \
    --enable-inews \
    --disable-rpath \
    --with-ssl \
    --enable-warnings
make %{?_smp_mflags}

%install
%make_install
install -m 644 -D doc/slrn.rc %{buildroot}%{_sysconfdir}/slrn/slrn.rc

# remove installed documentation, packaged manually below
rm -rf %{buildroot}%{_datadir}/doc

%find_lang %{name}

# make contrib scripts non-executable
find contrib/ doc -type f -exec chmod 644 {} +

%files
%license COPYING
%doc changes.txt COPYRIGHT README
%doc doc/{FAQ,FIRST_STEPS,help.txt,manual.txt,pc-keys.txt,README.GroupLens}
%doc doc/{README.macros,README.multiuser,README.SSL,score.txt,slrn-doc.html}
%doc doc/{slrnfuns.txt,slrn.rc,THANKS,*.sl}
%doc doc/slrnpull/ contrib/
%dir %{_sysconfdir}/slrn
%config(noreplace) %{_sysconfdir}/slrn/slrn.rc
%{_bindir}/slrn
%{_bindir}/slrnpull
%{_mandir}/man1/slrn.1%{?ext_man}
%{_mandir}/man1/slrnpull.1%{?ext_man}
%{_datadir}/slrn

%files lang -f %{name}.lang

%changelog
