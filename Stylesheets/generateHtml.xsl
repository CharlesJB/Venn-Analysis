<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
	<html>
	<head>
		<link rel="stylesheet" type="text/css">
			<xsl:attribute name='href'>Stylesheets/css/venn<xsl:value-of select="count(venn-analysis/sample)"/>.css</xsl:attribute>
		</link>
	</head>
	<body>
	<xsl:for-each select="venn-analysis">
		<xsl:for-each select="./sample">
			<div>
				<xsl:attribute name='class'>
				circle_venn<xsl:value-of select="count(//sample)"/>_<xsl:value-of select="position()"/>
				</xsl:attribute>
			</div>
			<p>
				<xsl:attribute name='class'>
				sample_venn<xsl:value-of select="count(//sample)"/>_<xsl:value-of select="position()"/>
				</xsl:attribute>
				<xsl:value-of select='.'/>
			</p>
		</xsl:for-each>
		<xsl:for-each select="./value">
			<p>
				<xsl:attribute name='class'>
				value_venn<xsl:value-of select="count(/venn-analysis/sample)"/>_<xsl:value-of select='name'/></xsl:attribute>
				<a>
					<xsl:attribute name='href'><xsl:value-of select='path'/></xsl:attribute>
					<xsl:attribute name='id'><xsl:value-of select='id'/></xsl:attribute>
					<xsl:value-of select='count'/>
				</a>
			</p>
		</xsl:for-each>
	</xsl:for-each>
	</body>
	</html>
</xsl:template>

</xsl:stylesheet>
