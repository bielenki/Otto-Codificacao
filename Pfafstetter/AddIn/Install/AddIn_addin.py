#! /usr/bin/python
# -*- coding: utf-8 -*-
import arcpy
import pythonaddins
import gdal
import fiona
import geopandas as gpd
import os.path
import sys, time, operator

def query_jusante (lyr, cobac, lista):
    Ncobacia = "Pfaf"
    Ncocurso = "cocurso"
    query = ""
    q = ""
    lista.sort()
    for x in lista:
        query = """{0} = '{1}' OR """.format(arcpy.AddFieldDelimiters(lyr,Ncocurso),x) + q
        q=query
    q = q[0:-4]
    q = "(" + q + ")"
    q = """{0} <= '{1}' and """.format(arcpy.AddFieldDelimiters(lyr,Ncobacia),cobac) + q
    query=unicode(q)
    return query

def query_montante (lyr, cobac, lista):
    Ncobacia = "Pfaf"
    Ncocurso = "cocurso"
    query = ""
    q = ""
    lista.sort()
    for x in lista:
        query = """{0} = '{1}' OR """.format(arcpy.AddFieldDelimiters(lyr,Ncocurso),x) + q
        q=query
    q = q[0:-4]
    q = "(" + q + ")"
    q = """{0} >= '{1}' and """.format(arcpy.AddFieldDelimiters(lyr,Ncobacia),cobac) + q
    query=unicode(q)
    return query

def COC (pfafstetter):
    i=-1
    for cont in range(len(pfafstetter)):
        if int(pfafstetter[i]) % 2 == 0:
            cocursodag= pfafstetter[:len(pfafstetter)-cont]
            break
        i=i-1
    return (cocursodag)

def COC_jusante (pfafstetter):
    # retorna uma lista de todos os cocursos a jusante
    lista=[]
    x=0
    for cont in range(len(pfafstetter)):
        if int(pfafstetter) % 2 == 0:
            lista.append(pfafstetter)
            x=+x
            pfafstetter=pfafstetter[:len(pfafstetter)-1]
        else:
            pfafstetter=pfafstetter[:len(pfafstetter)-1]
        if pfafstetter=='':
            break
    return (lista)

class ComboBoxClass_Layer(object):
    """Implementation for AddIn_layer.combobox (ComboBox)"""
    def __init__(self):
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWWWWWWWWWW'
        self.width = 'WWWWWWWWWWWWWW'
    def onSelChange(self, selection):
        global fc, fc_field
        fc = arcpy.mapping.ListLayers(self.mxd, selection)[0]
        fc_field = arcpy.ListFields(fc)
        pass
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        if focused:
		self.mxd = arcpy.mapping.MapDocument('current')
		layers = arcpy.mapping.ListLayers(self.mxd)
		self.items = []
		for layer in layers:
			self.items.append(layer.name)
        pass
    def onEnter(self):
        pass
    def refresh(self):
        pass

class ButtonClass_Jusante(object):
    """Implementation for AddIn_jusante.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        mxd = arcpy.mapping.MapDocument('current')
        df = arcpy.mapping.ListDataFrames(mxd)[0]
        lyr=fc
        desc=arcpy.Describe(lyr)
        Nr_sel=len(desc.FIDSet.split(";"))
        if Nr_sel==1 and desc.FIDSet=='' :
            pythonaddins.MessageBox(u'É necessário selecionar 1 trecho de drenagem', 'INFO', 0)
        elif Nr_sel>1:
            pythonaddins.MessageBox(u'É necessário selecionar apenas 1 trecho de drenagem', 'INFO', 0)
        elif Nr_sel==1 and desc.FIDSet<>'':
            cobacia_ini = arcpy.da.SearchCursor(lyr, "Pfaf").next()[0]
            cocurso_ini = COC(cobacia_ini)
            lista_cursos = COC_jusante(cobacia_ini)
            arcpy.SelectLayerByAttribute_management(lyr, "CLEAR_SELECTION")
            where_clause = "Pfaf <= '{}'".format(cobacia_ini)
            lista_cocursos=[]
            with arcpy.da.SearchCursor(lyr, 'Pfaf', where_clause) as cursor:
                for row in cursor:
                    cobacia=(row[0])
                    if COC(cobacia) in lista_cursos:
                        lista_cocursos.append(COC(cobacia))
            q=query_jusante(lyr,cobacia_ini,lista_cocursos)
            arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION" ,  unicode(q))
            df.zoomToSelectedFeatures()
        pass

class ButtonClass_cocurso(object):
    """Implementation for AddIn_cocurso.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        mxd = arcpy.mapping.MapDocument('current')
        df = arcpy.mapping.ListDataFrames(mxd)[0]
        lyr=fc
        arcpy.AddField_management(lyr,'cocurso','TEXT')
        cursor = arcpy.UpdateCursor(lyr)
        row = cursor.next()
        while row:
            row.setValue('cocurso', COC(row.getValue('Pfaf')))
            cursor.updateRow(row)
            row = cursor.next()
        pass

class ButtonClass_Montante(object):
    """Implementation for AddIn_montante.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        mxd = arcpy.mapping.MapDocument('CURRENT')
        df = arcpy.mapping.ListDataFrames(mxd,"*")
        activeDfName = mxd.activeDataFrame.name
        i = 0
        for d in df:
            if d.name == activeDfName:
                finalDf = arcpy.mapping.ListDataFrames(mxd,"*")[i]
            else:
                i +=1
        lyr=fc
        desc=arcpy.Describe(lyr)
        Nr_sel=len(desc.FIDSet.split(";"))
        if Nr_sel==1 and desc.FIDSet=='' :
            pythonaddins.MessageBox(u'É necessário selecionar 1 trecho de drenagem', 'INFO', 0)
        elif Nr_sel>1:
            pythonaddins.MessageBox(u'É necessário selecionar apenas 1 trecho de drenagem', 'INFO', 0)
        elif Nr_sel==1 and desc.FIDSet<>'':
            cobacia_ini = arcpy.da.SearchCursor(lyr, "Pfaf").next()[0]
            cocurso_ini=COC(cobacia_ini)
            NPfaf="Pfaf"
            Ncocurso="cocurso"
            arcpy.SelectLayerByAttribute_management(lyr, "CLEAR_SELECTION")
            query = """{0} >= '{1}' AND {2} LIKE '{3}%' """.format(arcpy.AddFieldDelimiters(lyr,NPfaf),cobacia_ini,arcpy.AddFieldDelimiters(lyr,Ncocurso),cocurso_ini)
            arcpy.SelectLayerByAttribute_management(lyr, "NEW_SELECTION", unicode(query))
            finalDf.zoomToSelectedFeatures()
        pass

class ButtonCodifica(object):
    """Implementation for AddIn_codifica.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        arcpy.AddToolbox(r'c:\Pfafstetter\AddIn\Install\Otto_Pfafstetter.tbx')
        toolboxName = 'Otto_Pfafstetter'
        toolName = 'Pfafstetter'
        toolboxPath = r'c:\Pfafstetter\AddIn\Install\Otto_Pfafstetter.tbx'
        pythonaddins.GPToolDialog(toolboxPath, toolName)
        pass

class ButtonClassAcumula(object):
    """Implementation for AddIn_Acumula.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        inicio = time.time()
        mxd = arcpy.mapping.MapDocument('current')
        df = arcpy.mapping.ListDataFrames(mxd)[0]
        lyr=fc
        field_name=field
        coluna=field_name+"_Acum"
        dfp=gpd.read_file(lyr.workspacePath+"\\"+lyr.name+".shp")
        dfp[coluna]=0
        for index, row in dfp.iterrows():
            cobac=row.Pfaf
            cocur=row.cocurso
            dfp_sel= dfp.loc[operator.and_(dfp.Pfaf>=cobac, dfp.cocurso.str.startswith(cocur))]
            soma = dfp_sel[field_name].sum()
            dfp.loc[index, coluna]= soma
            del dfp_sel
        output=lyr.workspacePath+"\\"+lyr.name+"_Acum.shp"
        dfp.to_file(driver = 'ESRI Shapefile', filename = output)
        newlayer = arcpy.mapping.Layer(output)
        arcpy.mapping.AddLayer(df, newlayer, "AUTO_ARRANGE")
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        fim=time.time()
        tempo=fim-inicio
        pythonaddins.MessageBox(u'Tempo de execução: ' + "%.2f" % tempo + ' segundos', 'INFO', 0)
        pass

class ComboBoxClassAtributo(object):
    """Implementation for AddIn_Atributo.combobox (ComboBox)"""
    def __init__(self):
        self.items = []
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWW'
        self.width = 'WWWWWW'
    def onSelChange(self, selection):
        global field
        field = selection
        pass
    def onEditChange(self, text):
        pass
    def onFocus(self, focused):
        if focused:
		self.mxd = arcpy.mapping.MapDocument('current')
		self.items = []
		for fields in fc_field:
			self.items.append(fields.name)
        pass
    def onEnter(self):
        pass
    def refresh(self):
        pass
