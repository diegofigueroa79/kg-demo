import streamlit as st


#from docparser import split_documents
#from prompts import construct_prompt
from ontology import get_ontology
#from graph_merger import join_graphs


import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader



def authenticate():
    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    name, authentication_status, username = authenticator.login()
    if st.session_state["authentication_status"]:
        authenticator.logout('Logout', 'main', key='unique_key')
        with open('./config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)
        st.write(f'Welcome *{st.session_state["name"]}*')
        main()
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')
    return name, authentication_status, username

def main():

    col1, col2 = st.columns([0.4, 0.6])

    with col1:
        #uploaded_file = st.file_uploader("Choose a file")
        file_link = st.text_input(
            label="Document Link", 
            key="file_link", 
            value="https://raw.githubusercontent.com/skarlekar/graph-visualizer/1927533f5b79fd1fd529944d77462553e7fe9bde/content/Appraisal-Report.pdf"
        )

        ontology = st.text_input(
            label="Ontology Link", 
            key="ontology_link",
            value="https://raw.githubusercontent.com/skarlekar/graph-visualizer/main/ontologies/PropertyAppraisalOntology-v2.ttl"
        )

    with col2:
        if st.button("Generate Graph"):
            if file_link and ontology:
                #loader = PyPDFLoader(file_link)
                #pages = loader.load_and_split()
                #doc = loader.load()
                #texts = split_documents(chunk_size=1000, document=doc)

                tab1, tab2, tab3, tab4 = st.tabs(["Graph 1", "Graph 2", "Graph3", "Merged Graph"])

                with tab1:
                    #prompt = construct_prompt(ontology=ontology, text=texts[0].page_content)
                    #response = llm.invoke(input=prompt)
                    st.text(f"""@prefix ns1: <https://raw.githubusercontent.com/skarlekar/graph-visualizer/main/ontologies/> . 
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> . 

<mf:PropertyAppraisal_1> a <mf:PropertyAppraisal> ; 
    ns1:hasAppraisedValue "current market value" ; 
    ns1:hasAppraiser "jason p. shirey, mai, ccim, cpm", "josette d. jackson, ccim" ; 
    ns1:hasDate "2019-04-16" ; 
    ns1:hasRemarks "equivalue appraisal llc professional appraisal and valuation services po box 5326 destin, florida 32540 phone (850) 424-6119" ; 
    ns1:hasTitle "appraisal report" . 
    
<mf:PropertyBuildingType_1> a <mf:PropertyBuildingType> ; 
    rdfs:label "a 62 unit multi-family residential property" . 

<mf:SubjectProperty_1> a <mf:SubjectProperty> ; 
    ns1:hasAddress <mf:PropertyAddress_1> ; 
    ns1:hasName "college courtyard apartments & raider housing" ; 
    ns1:hasUnits "62" . 

<mf:PropertyAddress_1> a <mf:PropertyAddress> ; 
    ns1:hasCity "niceville" ; 
    ns1:hasState "fl" ; 
    ns1:hasStreetName "garden lane" ; 
    ns1:hasStreetNumber "28", "30" ; 
    ns1:hasZip "32578" .""")
                
                with tab2:
                    #prompt2 = construct_prompt(ontology=ontology, text=texts[1].page_content)
                    #response2 = llm.invoke(input=prompt2)
                    #st.divider()
                    st.text(f"""@prefix ns1: <https://raw.githubusercontent.com/skarlekar/graph-visualizer/main/ontologies/> . 
                    
<mf:PropertyAppraisalDate_1> a <mf:PropertyAppraisalDate> ; 
    ns1:hasDay "10" ; 
    ns1:hasMonth "january" ; 
    ns1:hasYear "2020" . 

<mf:PropertyAppraisal_1> a <mf:PropertyAppraisal> ; 
    ns1:hasAppraisedValue "current market value" ; 
    ns1:hasAppraiser "jason p. shirey, mai, ccim state certified general real estate appraiser rz3186", "josette d. jackson, ccim state certified general real estate appraiser rz3275" ; 
    ns1:hasDate "2019-12-13" ; 
    ns1:hasRemarks "of existing multi-family property" ; 
    ns1:hasTitle "appraisal report" . 

<mf:PropertyInspectionDate_1> a <mf:PropertyInspectionDate> ; 
    ns1:hasDay "13" ; ns1:hasMonth "december" ; 
    ns1:hasYear "2019" . 

<mf:SubjectProperty_1> a <mf:SubjectProperty> ; 
    ns1:hasAddress <mf:PropertyAddress_1> ; 
    ns1:hasName "college courtyard apartments & raider housing" ; 
    ns1:hasOwner "ms. cristie kedroski vice president of college advancement northwest florida state college foundation" ; 
    ns1:hasUnits "62 unit multi-family property" . 

<mf:PropertyAddress_1> a <mf:PropertyAddress> ; 
    ns1:hasCity "niceville" ; 
    ns1:hasState "fl" ; 
    ns1:hasStreetName "garden lane" ; 
    ns1:hasStreetNumber "28", "30" ; 
    ns1:hasZip "32578" .""")
                
                with tab3:
                    #st.divider()
                    #joined_graph = join_graphs(graph1=response.content, graph2=response2.content, llm=llm)
                    st.text(f"""@prefix ns1: <https://raw.githubusercontent.com/skarlekar/graph-visualizer/main/ontologies/> . 
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> . 

<mf:PropertyAppraisalDate_1> a <mf:PropertyAppraisalDate> ; 
    ns1:hasDay "13"^^<mf:PropertyAppraisalDay> ; 
    ns1:hasMonth "12"^^<mf:PropertyAppraisalMonth> ; 
    ns1:hasYear "2019"^^<mf:PropertyAppraisalYear> . 

<mf:PropertyAppraisal_1> a <mf:PropertyAppraisal> ; 
    ns1:hasAppraisedValue "Five Million Dollars ($5,000,000)"^^<mf:NamedEntity> ; 
    ns1:hasAppraiser "Jason P. Shirey, MAI , CCIM"^^<mf:NamedEntity>, "Josette D. Jackson , CCIM"^^<mf:NamedEntity> ; 
    ns1:hasDate "2019-12-13"^^<mf:PropertyAppraisalDate> ; 
    ns1:hasRemarks "The estimated market exposure period necessary for the subject to have achieved this value is estimated to be 9-12 months ."^^<mf:PropertyAppraisalRemarks> ; 
    ns1:hasTitle "Current Market Value of the Fee Simple Interest In the Subject Property, In 'As Is' Condition, As of December 13, 2019"^^xsd:string .""")

                with tab4:
                    st.text(f"""@prefix ns1: <https://raw.githubusercontent.com/skarlekar/graph-visualizer/main/ontologies/> . 
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> . 

<mf:PropertyAppraisalDate_1> a <mf:PropertyAppraisalDate> ; 
    ns1:hasDay "10" ; 
    ns1:hasMonth "january" ; 
    ns1:hasYear "2020" . 

<mf:PropertyAppraisal_1> a <mf:PropertyAppraisal> ; 
    ns1:hasAppraisedValue "current market value" ; 
    ns1:hasAppraiser "jason p. shirey, mai, ccim state certified general real estate appraiser rz3186", "jason p. shirey, mai, ccim, cpm", "josette d. jackson, ccim", "josette d. jackson, ccim state certified general real estate appraiser rz3275" ; 
    ns1:hasDate "2019-04-16", "2019-12-13" ; 
    ns1:hasRemarks "equivalue appraisal llc professional appraisal and valuation services po box 5326 destin, florida 32540 phone (850) 424-6119", "of existing multi-family property" ; 
    ns1:hasTitle "appraisal report" . 

<mf:PropertyBuildingType_1> a <mf:PropertyBuildingType> ; 
    rdfs:label "a 62 unit multi-family residential property" . 

<mf:PropertyInspectionDate_1> a <mf:PropertyInspectionDate> ; 
    ns1:hasDay "13" ; 
    ns1:hasMonth "december" ; 
    ns1:hasYear "2019" . 

<mf:SubjectProperty_1> a <mf:SubjectProperty> ; 
    ns1:hasAddress <mf:PropertyAddress_1> ; 
    ns1:hasName "college courtyard apartments & raider housing" ; 
    ns1:hasOwner "ms. cristie kedroski vice president of college advancement northwest florida state college foundation" ; 
    ns1:hasUnits "62", "62 unit multi-family property" . 

<mf:PropertyAddress_1> a <mf:PropertyAddress> ; 
    ns1:hasCity "niceville" ; 
    ns1:hasState "fl" ; 
    ns1:hasStreetName "garden lane" ; 
    ns1:hasStreetNumber "28", "30" ; 
    ns1:hasZip "32578" .""")
            else:
                st.error('Document or ontology is missing', icon="🚨")

if __name__ == '__main__':
    st.set_page_config(layout="wide")
    authenticate()
