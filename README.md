# Testobjekt für die Testautomatisierung

## Inhaltsverzeichis

- [Testobjekt für die Testautomatisierung](#testobjekt-für-die-testautomatisierung)
  - [Inhaltsverzeichis](#inhaltsverzeichis)
  - [Übersicht](#übersicht)
  - [Was ist das Testobjekt](#was-ist-das-testobjekt)
    - [Einsatzbereich und Zielgruppe](#einsatzbereich-und-zielgruppe)
    - [Ungeeignete Anwendungsbereiche](#ungeeignete-anwendungsbereiche)
    - [Welche Versionen gibt es](#welche-versionen-gibt-es)
    - [Besonderheiten des Testobjekts](#besonderheiten-des-testobjekts)
    - [Programmiersprachen und Frameworks](#programmiersprachen-und-frameworks)
    - [Datenbanken](#datenbanken)
    - [Wie kommen User Stories und Nutzer in das Testobjekt](#wie-kommen-user-stories-und-nutzer-in-das-testobjekt)
  - [Anleitung zur Nutzung](#anleitung-zur-nutzung)
    - [Installation der Abhängigkeiten](#installation-der-abhängigkeiten)
    - [Starten der Anwendung](#starten-der-anwendung)
    - [Zugriff auf die Anwendung](#zugriff-auf-die-anwendung)
  - [Hinweise zur Weiterentwicklung](#hinweise-zur-weiterentwicklung)
  - [Support und Kontakt](#support-und-kontakt)

## Übersicht

Das Testobjekt wird entwickelt, um eine praxisnahe Testumgebung für die Automatisierung von Softwaretests bereitzustellen. Es ermöglicht insbesondere Studierenden und Entwicklern, ihre Kenntnisse im Bereich der Testautomatisierung zu vertiefen und anzuwenden.

## Was ist das Testobjekt

### Einsatzbereich und Zielgruppe

Das Testobjekt ist ein Tool zur Unterstützung der Ausbildung und Praxis im Bereich der Testautomatisierung. Es bietet eine lokale, isolierte Umgebung, in der Nutzer ihre Testautomatisierungsfähigkeiten entwickeln und testen können.

### Ungeeignete Anwendungsbereiche

Dieses Repository enthält lediglich einen Entwicklungsstand zu Übungszwecken und sollte unter keinen Umständen in einer Produktivumgebung eingesetzt werden.
Dieses Webentwicklungsprojekt wurde ausschließlich zu Lern- und Testzwecken erstellt und wird in einem öffentlichen Repository gehostet. Der bereitgestelten Codes sollte in seiner hier bereitgestellten Form **nicht** in einer Produktivumgebung eingesetzt werden. Es wird keine Garantie für die Funktionsfähigkeit oder Sicherheit der Anwendung übernommen. Der Code steht unter der MIT-Lizenz und kann frei verwendet und modifiziert werden, solange die Urheberrechte beachtet werden. Für Schäden, die durch die Nutzung oder Fehlfunktion der Anwendung entstehen, wird keine Haftung übernommen. Fragen oder Anmerkungen zu diesem Projekt können über das Projektteam *ProPra* mitgeteilt werden.

### Welche Versionen gibt es

Es werden 3 Versionen des Testobjekt umgesetzt, die aus Übungszwecken Auswirkunegna auf die zu entwickelden Testfälle haben werden.

- Version 1.0.0: Eine einfache Web-Lösung.
- Version 1.1.0: Erweiterte Funktionalitäten und Bugfixes.
- Version 3.0.0: Umfassende Änderungen in der Architektur und Entwicklungsstrategie.

### Besonderheiten des Testobjekts

Eine Besonderheit des Testobjekts ist die Integration von User Stories, die eine unmittelbare Darstellung der Entwicklungsanforderungen ermöglicht. Dies erleichtert die Arbeit ohne ein separates Ticket-Management-Tool und bietet den Vorteil, Anforderungen direkt im Kontext des Testobjekts zu sehen. Dieser Teil der Entwicklung wird als systemrelevant betrachtet und kann bei Bedarf ausgeblendet werden.

![Testobjekt Version 1.0.0](images/testobject_requirements.gif)

Auf der anderen Seite bietet das Testobjekt speziell für Lern- und Übungszwecke konzipierte Funktionen. Übungsaufgaben beziehen sich auf diesen Anwendungsbereich.

### Programmiersprachen und Frameworks

Um den Lerninhalt des Programmierpraktikums (ProPra) effektiv zu unterstützen, wird das Testobjekt unter Verwendung von Python in der aktuellsten Version entwickelt. Durch den Einsatz des Python-Webframeworks Flask erstellen wir eine Web-Applikation, die speziell auf die im ProPra definierten Aufgaben und Anforderungen abgestimmt ist.

Die Anwendung nutzt zudem eine Kombination aus HTML und CSS, um eine benutzerfreundliche und visuell ansprechende Oberfläche zu gestalten. Durch den Einsatz von HTML erreichen wir eine strukturierte und semantisch korrekte Darstellung der Inhalte, während CSS für die stilistische Gestaltung und das Responsive Design der Anwendung sorgt.

Darüber hinaus verwenden wir Bootstrap, ein weit verbreitetes Front-End-Framework, um eine konsistente und responsive Benutzeroberfläche zu schaffen. Bootstrap bietet eine Vielzahl von vorgefertigten Komponenten und Layout-Optionen, die es uns ermöglichen, das Design effizient und effektiv umzusetzen, ohne von Grund auf neu beginnen zu müssen.

Ebenfalls integrieren wir kleine, aber entscheidende Teile in JavaScript, um interaktive Elemente in der Web-Applikation zu ermöglichen. Diese Integration von JavaScript ermöglicht es uns, eine dynamischere Benutzererfahrung zu schaffen, indem wir clientseitige Skripte verwenden, die auf Benutzeraktionen reagieren und ohne eine vollständige Neuladung der Seite Updates vornehmen können.

Die Kombination dieser Technologien - Python, Flask, HTML, CSS, Bootstrap und JavaScript - ermöglicht es uns, eine robuste, funktionale und benutzerfreundliche Testumgebung zu schaffen, die sowohl die Lernziele des ProPra-Programms unterstützt als auch den Anwender eine ansprechende Erfahrung bietet.

### Datenbanken

Für die Verwaltung der Testdaten setzen wir auf die Verwendung von SQL in Verbindung mit der SQL-Alchemie-Datenbank. Diese Kombination ermöglicht es uns, Daten effizient zu speichern, abzurufen und zu verwalten. Bei jedem Start der Anwendung wird automatisch überprüft, ob die erforderlichen Testdaten vorhanden sind.

Sollten die Testdaten fehlen – beispielsweise weil sie durch Testskripte gelöscht wurden – werden sie automatisch neu in die Datenbank eingespielt. Dieser Prozess gewährleistet, dass die Anwendung stets mit den notwendigen Daten versorgt ist und ermöglicht ein effizientes Testen ohne manuellen Eingriff.

Die Datenbankdateien werden im Verzeichnis instance/ gespeichert. Diese Strukturierung bietet den Vorteil, dass die Datenbankdateien bei Bedarf einfach und sicher gelöscht werden können, falls unerwartete Probleme auftreten sollten. Diese Flexibilität in der Datenbankhandhabung erleichtert die Wartung und Fehlerbehebung und macht die Anwendung robust gegenüber unvorhergesehenen Datenproblemen.

Durch diese Konfiguration stellen wir sicher, dass die Testumgebung jederzeit reproduzierbare und konsistente Ergebnisse liefert, was für die Zuverlässigkeit und Genauigkeit der Testautomatisierung von entscheidender Bedeutung ist.

### Wie kommen User Stories und Nutzer in das Testobjekt

Die Integration von User Stories und Nutzer in das Testobjekt erfolgt durch einen strukturierten und automatisierten Prozess. Zunächst werden die User Stories in einer JSON-Datei gespeichert, die sich im Verzeichnis 'data' befindet. Diese JSON-Datei dient als zentrale Quelle für die Testdaten und enthält alle notwendigen Informationen zu den User Stories oder Nutzern, wie etwa Beschreibungen, Akzeptanzkriterien und Nutzerdaten.

Bei der Initialisierung der Datenbank, die durch Flask gesteuert wird, wird diese JSON-Datei ausgelesen. Flask bietet hierfür passende Funktionen, um die Daten aus der JSON-Datei effizient zu extrahieren und zu verarbeiten. Nach dem Auslesen der Daten erfolgt eine Transformation, bei der die Daten in ein Format umgewandelt werden, das mit der Struktur der SQL-Alchemie-Datenbank kompatibel ist.

Anschließend werden die so aufbereiteten Daten in die Datenbank eingespielt. Dieser Vorgang findet typischerweise beim ersten Start der Anwendung statt oder kann bei Bedarf auch manuell ausgelöst werden. Durch diesen Mechanismus stellen wir sicher, dass die Datenbank stets mit den definierten Daten gefüllt ist, die dann im Rahmen der Testautomatisierung verwendet werden können.

Die Verwendung einer JSON-Datei als Quelle für die Daten bietet mehrere Vorteile: Sie ermöglicht eine einfache Handhabung und Bearbeitung der Testdaten und unterstützt die Transparenz sowie die Nachvollziehbarkeit der Daten. Zudem erleichtert diese Methode die Aktualisierung und Erweiterung der Daten, da lediglich die JSON-Datei angepasst werden muss, ohne die Notwendigkeit, direkt in die Datenbank einzugreifen.

## Anleitung zur Nutzung

Bevor Sie mit der Nutzung des Testobjekts beginnen, stellen Sie sicher, dass Python 3 und das Web-Framework Flask in der neuesten Version auf Ihrem System installiert sind. Diese sind grundlegende Voraussetzungen für den Betrieb der Anwendung.

### Installation der Abhängigkeiten

Jede Version des Testobjekts kann spezifische Abhängigkeiten haben. Daher verfügt jede Version über eine eigene requirements.txt-Datei, die alle notwendigen Pakete auflistet. Führen Sie den folgenden Befehl aus, um die erforderlichen Pakete für die gewählte Version zu installieren:

```shell
pip install -r v[Version]/requirements.txt 
```

Ersetzen Sie [Version] durch 1.0.0, 1.1.0 oder 3.0.0, je nachdem, welche Version Sie verwenden möchten.

### Starten der Anwendung

Nach der Installation der Abhängigkeiten können Sie die Anwendung mit folgendem Befehl starten:

```shell
flask --app v[Version]/app run
```

Ersetzen Sie erneut [Version] durch die gewünschte Version. Zum Beispiel:

- Für Version 1.0.0: flask --app v1.0.0/app run
- Für Version 1.1.0: flask --app v1.1.0/app run
- Für Version 3.0.0: flask --app v3.0.0/app run

### Zugriff auf die Anwendung

Nachdem die Anwendung gestartet wurde, können Sie darauf zugreifen, indem Sie die folgende URL in Ihrem Webbrowser eingeben:

```URL
http://127.0.0.1:5000
```

Dies öffnet die Hauptseite der Anwendung, auf der Sie mit der Interaktion beginnen können.

## Hinweise zur Weiterentwicklung

Die Testobjekte unterliegen einer kontinuierlichen Weiterentwicklung, wobei sowohl neue Features zur Unterstützung der Testautomatisierungsübungen als auch systemrelevante Änderungen implementiert werden können. Unabhängig von der Art der Änderung ist es essenziell, die Dokumentation stets aktuell zu halten. Folgende Punkte sollten beachtet werden:

- Jede Änderung oder Ergänzung am Testobjekt sollte von einer entsprechenden Aktualisierung der Dokumentation begleitet sein. Dies umfasst technische Details, Benutzeranleitungen und Beschreibungen neuer Features oder Veränderungen.
- Wichtige Änderungen sollten innerhalb des Teams und an die Nutzer kommuniziert werden. Dies hilft dabei, alle Beteiligten auf dem Laufenden zu halten und das Verständnis für die Entwicklung des Projekts zu fördern.

## Support und Kontakt

Falls Sie auf unerwartete Probleme oder Fehler in der Anwendung stoßen – abgesehen von den bewusst für Übungszwecke integrierten Störungen, die in den User Stories beschrieben sind –, laden wir Sie herzlich ein, dies über das GitHub Issue-System zu melden. Ihre Rückmeldungen sind für uns von großem Wert und tragen entscheidend zur kontinuierlichen Verbesserung des Testobjekts bei.

Bitte beschreiben Sie das Problem so detailliert wie möglich, inklusive der Schritte, die zu dem Fehler geführt haben, sowie alle relevanten Informationen, die uns helfen könnten, das Problem zu reproduzieren und zu beheben. Jedes Issue wird sorgfältig geprüft und, falls notwendig, in den Entwicklungsprozess integriert, um eine schnelle und effektive Lösung zu gewährleisten. (Sollten Sie unsicher sein, wie ein Issue / Defect formuliert wird, nutzen Sie doch die Gelegenheit das daszu im ProPra umgestezte Thema kennenzulernen.)

Ihr Engagement und Ihre Unterstützung sind essentiell für die Qualität und Zuverlässigkeit des Testobjekts. Wir schätzen jede Form von Feedback und freuen uns auf Ihre aktive Beteiligung an unserem Projekt.
