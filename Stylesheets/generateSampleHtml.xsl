<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
	<html>
	<head>
	</head>
	<body>
	<xsl:for-each select="venns">
		<xsl:for-each select="./combination">
			<a>
				<xsl:attribute name='href'><xsl:value-of select='path'/></xsl:attribute>
				<xsl:value-of select='name'/>
			</a>
		</xsl:for-each>
	</xsl:for-each>
	</body>
	</html>
</xsl:template>
</xsl:stylesheet>
