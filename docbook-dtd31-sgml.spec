Summary:	DocBook - DTD for technical documentation
Summary(pl.UTF-8):	DocBook - DTD przeznaczone do pisania dokumentacji technicznej
%define ver	3.1
%define sver	31
Name:		docbook-dtd%{sver}-sgml
Version:	1.0
Release:	16
Vendor:		OASIS
License:	Free
Group:		Applications/Publishing/SGML
URL:		http://www.oasis-open.org/docbook/
Source0:	http://www.oasis-open.org/docbook/sgml/%{ver}/docbk%{sver}.zip
# Source0-md5:	432749c0c806dbae81c8bcb70da3b5d3
BuildRequires:	unzip
Requires(post,postun):	sgml-common >= 0.5
Requires:	sgmlparser
Requires:	sgml-common >= 0.5
Provides:	docbook-dtd
Obsoletes:	docbook%{sver}-dtd
Obsoletes:	docbook-sgml-%{ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DocBook - DTD for technical documentation.

%description -l pl.UTF-8
DocBook DTD jest zestawem definicji dokumentów przeznaczonych do
tworzenia dokumentacji programistycznej. Stosowany jest do pisania
podręczników systemowych, instrukcji technicznych jak i wielu innych
ciekawych rzeczy.

%prep
%setup -q -c
chmod 644 *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/sgml-dtd-%{ver}

install *.dtd *.mod *.dcl $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/sgml-dtd-%{ver}/

# install catalog (but filter out ISO entities)
grep -v 'ISO ' docbook.cat > $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/sgml-dtd-%{ver}/catalog


%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- %{name} < 1.0-13
if ! grep -q /etc/sgml/sgml-docbook-%{ver}.cat /etc/sgml/catalog ; then
	/usr/bin/install-catalog --add /etc/sgml/sgml-docbook-%{ver}.cat /usr/share/sgml/docbook/sgml-dtd-%{ver}/catalog > /dev/null
fi

%post
if ! grep -q /etc/sgml/sgml-docbook-%{ver}.cat /etc/sgml/catalog ; then
	/usr/bin/install-catalog --add /etc/sgml/sgml-docbook-%{ver}.cat /usr/share/sgml/docbook/sgml-dtd-%{ver}/catalog > /dev/null
fi

%postun
if [ "$1" = "0" ] ; then
	/usr/bin/install-catalog --remove /etc/sgml/sgml-docbook-%{ver}.cat /usr/share/sgml/docbook/sgml-dtd-%{ver}/catalog > /dev/null
fi

%files
%defattr(644,root,root,755)
%doc *.txt ChangeLog
%{_datadir}/sgml/docbook/*
