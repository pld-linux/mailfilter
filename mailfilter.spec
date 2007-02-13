Summary:	Antispam utility
Summary(pl.UTF-8):	Narzędzie antyspamowe
Name:		mailfilter
Version:	0.6.2
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	0c03ef7f9ff214b034eaaf68515610aa
Source1:	%{name}-pl.po
Patch0:		%{name}-home_etc.patch
URL:		http://mailfilter.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	 -fomit-frame-pointer 

%description
Mailfilter is a flexible utility for Unix (-like) operating systems to
get rid of unwanted spam mails, before having to go through the
trouble of downloading them into the local computer. It offers support
for one or many POP3 accounts and is especially useful for dialup
connections via modem, ISDN, etc.
Mailfilter connects to any POP3 mail box and compares part of its
content to a set of user defined filter rules. That way the spam gets
deleted directly on the mail server.

%description -l pl.UTF-8
Mailfilter jest elastycznym narzędziem dla systemów UNIXopodobnych,
służącym do pozbywania się niechcianego spamu przed pobraniem go na
lokalny komputer z sieci. Obsługuje wiele kont POP3 i jest nadzwyczaj
użyteczny dla połączeń wdzwanianych przez modem, ISDN etc.
Mailfilter łączy się z kontem POP3 i porównuje części jego zawartości
z zestawem regułek zdefiniowanych przez użytkownika. W ten sposób spam
zostaje usunięty bezpośrednio na serwerze pocztowym.

%prep
%setup -q
%patch0 -p1
install %{SOURCE1} po/pl.po

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5}}

make install DESTDIR=$RPM_BUILD_ROOT
install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install man/*.5 $RPM_BUILD_ROOT%{_mandir}/man5
mv -f doc/api/man/man3 $RPM_BUILD_ROOT%{_mandir}
rm -rf doc/api/man

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS THANKS TODO doc/{api,Doxyfile,FAQ,rcfile.example{1,2},supported_servers}
%lang(it) %doc doc/rcfile.example1.it
%lang(ru) %doc doc/rcfile.example2.ru
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
