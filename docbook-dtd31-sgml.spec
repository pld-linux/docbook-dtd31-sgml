Summary:	DocBook - DTD for technical documentation
Summary(pl):	DocBook - DTD przeznaczone do pisania dokumentacji technicznej 
%define ver	3.1
%define sver	31
Name:		docbook-dtd%{sver}-sgml
Version:	1.0
Release:	12
Vendor:		OASIS
License:	Free
Group:		Applications/Publishing/SGML
URL:		http://www.oasis-open.org/docbook/
Source0:	http://www.oasis-open.org/docbook/sgml/%{ver}/docbk%{sver}.zip
Prereq:		sgml-common >= 0.5
Requires:	sgmlparser
Provides:	docbook-dtd
Obsoletes:	docbook%{sver}-dtd
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	docbook-sgml-%{ver}

%description
DocBook - DTD for technical documentation.

%description -l pl 
DocBook DTD jest zestawem definicji dokumentów przeznaczonych do
tworzenia dokumentacji programistycznej. Stosowany jest do pisania
podrêczników systemowych, instrukcji technicznych jak i wielu innych
ciekawych rzeczy.

%prep
%setup -q -c -T 
unzip -qa %{SOURCE0}
chmod 644 *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/sgml-dtd-%{ver}

install *.dtd *.mod *.dcl $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/sgml-dtd-%{ver}

# install catalog (but filter out ISO entities)
grep -v 'ISO ' docbook.cat > $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/sgml-dtd-%{ver}/catalog

gzip -9nf *.txt
[ ! -f ChangeLog ] || gzip -9nf ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post
# Update the centralized catalog corresponding to this version of the DTD
/usr/bin/install-catalog --add /etc/sgml/sgml-docbook-%{ver}.cat /usr/share/sgml/docbook/sgml-dtd-%{ver}/catalog > /dev/null

%postun
/usr/bin/install-catalog --remove /etc/sgml/sgml-docbook-%{ver}.cat /usr/share/sgml/docbook/sgml-dtd-%{ver}/catalog > /dev/null

%files
%defattr(644,root,root,755)
%doc *.gz 
%{_datadir}/sgml/docbook/*
