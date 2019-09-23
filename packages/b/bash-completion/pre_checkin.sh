#!/bin/sh

if test bash-completion.spec -ot bash-completion-doc.spec ; then
	echo "bash-completion.spec is older than bash-completion-doc.spec. Please merge changes manually and call pre-checkin.sh again."
	exit 1
fi
if test bash-completion.changes -ot bash-completion-doc.changes ; then
	echo "bash-completion.changes is older than bash-completion-doc.changes. Please merge changes manually and call pre-checkin.sh again."
	exit 1
fi

SUMMARY_DOC="$(sed -n '/^%package doc/,/^%description doc/{/^Summary:/p;}' bash-completion.spec)"
GROUP_DOC="$(sed -n '/^%package doc/,/^%description doc/{/^Group:/p;}' bash-completion.spec)"

sed '
	s/spec file for package bash-completion/spec file for package bash-completion-doc/;
	/^Name:/s/bash-completion/bash-completion-doc/;
	s/WARNING: After editing this file please/WARNING: Never edit this file!!! Edit bash-completion.spec and/;
	s/%{name}/%{_name}/g;
	s@^Summary:.*$@'"$SUMMARY_DOC"'@
	s@^Group:.*$@'"$GROUP_DOC"'@
	/^%package doc/,/^%description doc/{/^Summary:/d;/^Group:/d;}
	s/^%setup -q$/%setup -q -n %{_name}-%{version}/
	/^# Do not change %%build_core./d
	/## Always set %%build_doc/d
	/^Name:/a %define _name bash-completion
	/^%define build_core/d
	/^%define build_doc/d
	/^%if %build_core$/,/^%endif %build_core$/d
	/^%if %build_doc$/d
	/^%endif %build_doc$/d
	/^%package doc$/d
	s/^%\(description\|files\) doc$/%\1/
	/^$/H
	# Delete trailing dual empty line as it causes overwritting by spec formatter:
	\:^%{_defaultdocdir}/%{_name}/html/:,/^%changelog/{/^$/H;/^$/D;\:^%{_defaultdocdir}/%{_name}/html/:a
}
' <bash-completion.spec >bash-completion-doc.spec

cp -a bash-completion.changes bash-completion-doc.changes

touch bash-completion.spec bash-completion.changes
