from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from runner import run
from preset_manager import create_preset, load_preset, load_all_presets, inverse_of_web_parameter_formatting, delete_presets

# hide all widgets
def hide_all_widgets():
    s_a_p_label.hide()
    s_a_p.hide()
    s_a_p_req_type.hide()
    s_a_p_button.hide()
    s_a_p_list.hide()
    s_a_p_list_edit_button.hide()
    s_a_p_list_delete_button.hide()

    e_t_s_label.hide()
    e_t_s_elem.hide()
    e_t_s_attrs.hide()
    e_t_s_attrs_values.hide()
    e_t_s_for_site.hide()
    e_t_s_add_button.hide()
    e_t_s_list.hide()
    e_t_s_list_edit_button.hide()
    e_t_s_list_delete_button.hide()

    w_r_p_label.hide()
    w_r_p_site_label.hide()
    w_r_p_site.hide()
    w_r_p_select_label.hide()
    w_r_p_select.hide()
    w_r_p_add_param.hide()
    w_r_p_add_param_value.hide()
    w_r_p_list.hide()
    w_r_p_list_edit.hide()
    w_r_p_add_button.hide()

    p_s_r_label.hide()
    p_s_r_create_label.hide()
    p_s_r_create_button.hide()
    p_s_r_load_label.hide()
    p_s_r_load_button.hide()
    p_s_r_delete_preset_button.hide()
    p_s_r_load_list.hide()
    p_s_r_load_into_run_button.hide()

    s_p_a_title.hide()
    s_p_a_adding_box_label.hide()
    s_p_a_adding_box.hide()
    s_p_a_url_label.hide()
    s_p_a_url_selection.hide()
    s_p_a_adding_button.hide()
    s_p_a_list.hide()

    ask.hide()
    show_site_list_l.hide()
    show_site_list.hide()
    show_elems_list_l.hide()
    show_elems_list.hide()
    yes_button.hide()
    no_button.hide()


def display_set_site_controls():
    hide_all_widgets()

    s_a_p.show()
    s_a_p_req_type.show()
    s_a_p_label.show()
    s_a_p_button.show()
    s_a_p_list.show()
    s_a_p_list_edit_button.show()
    s_a_p_list_delete_button.show()

def display_set_payloads_controls():
    hide_all_widgets()

    w_r_p_label.show()
    w_r_p_site_label.show()
    w_r_p_site.show()
    w_r_p_select_label.show()
    w_r_p_select.show()
    w_r_p_add_param.show()
    w_r_p_add_param_value.show()
    w_r_p_list.show()
    w_r_p_list_edit.show()
    w_r_p_add_button.show()

def display_set_elements_to_scrape():
    hide_all_widgets()

    e_t_s_label.show()
    e_t_s_elem.show()
    e_t_s_attrs.show()
    e_t_s_attrs_values.show()
    e_t_s_for_site.show()
    e_t_s_add_button.show()
    e_t_s_list.show()
    e_t_s_list_edit_button.show()
    e_t_s_list_delete_button.show()

def display_presets_controls():
    hide_all_widgets()

    p_s_r_label.show()
    p_s_r_create_label.show()
    p_s_r_create_button.show()
    p_s_r_load_label.show()
    p_s_r_load_button.show()
    p_s_r_load_list.show()
    p_s_r_delete_preset_button.show()
    p_s_r_load_into_run_button.show()

def display_proxy_controls():
    hide_all_widgets()

    s_p_a_title.show()
    s_p_a_adding_box_label.show()
    s_p_a_adding_box.show()
    s_p_a_url_label.show()
    s_p_a_url_selection.show()
    s_p_a_adding_button.show()
    s_p_a_list.show()

def display_final_button():
    hide_all_widgets()

    show_site_list.clear()
    show_elems_list.clear()

    to_show_sites = [i['url'] for i in site_list]
    to_show_elems = [f"{i['name']}\n{i['for site']}" for i in elements_list]

    show_site_list.addItems(to_show_sites)
    show_elems_list.addItems(to_show_elems)
    
    ask.show()
    show_site_list_l.show()
    show_site_list.show()
    show_elems_list_l.show()
    show_elems_list.show()
    yes_button.show()
    no_button.show()

def reset_app():
    s_a_p_list.clear()
    e_t_s_list.clear()
    w_r_p_list.clear()
    show_site_list.clear()
    show_elems_list.clear()

    site_list.clear()
    elements_list.clear()
    payloads_list.clear()

    e_t_s_for_site.clear()
    e_t_s_for_site.addItem("Select site this element belongs to")

    w_r_p_site.clear()
    w_r_p_site.addItem('Select Site')

    display_set_site_controls()

#------------------------------------------------------------------------------------------

# function that creates a preset
def create_preset_():
    # checks if the site list is 0; what preset is user tryna create?
    if len(site_list) == 0:
        alert.setText("Error")
        alert.setInformativeText("Enter data to be presetted")
        alert.exec_()
    # then if it is greater than one; only one URL at a time
    elif len(site_list) > 1:
        alert.setText("Warning")
        alert.setInformativeText("More than one URLs detected trying to be added into a preset. PRESETTING ONLY WORKS WITH ONE URL AT A TIME.")
        alert.exec_()
    else:
        name, _ = preset_name_asker.getText(display_frame, "Preset Name?", "Enter the name of the Preset.")
        create_preset(
            preset_name=name,
            url_list=site_list,
            elements=elements_list,
            payloads=payloads_list
        )

def loading_all_the_presets():
    p_s_r_load_list.clear()
    c = load_all_presets()

    if c == "Table doesnt exist":
        alert.setText("Error")
        alert.setInformativeText("Table in the database doesnt exist. Most likely means that no presets actually exist. Create a preset first")
        alert.exec_()
    else:
        for i in c:
            name = i[0]
            site = i[1]
            req_type = i[2]
            if "/|\\" in i[3]:
                elements = str(i[3]).split("/|\\")
                elements = [i.split("|") for i in elements]
            else:
                elements = str(i[3]).split("|")
            
            if "///" in i[4]:
                parameters = str(i[4]).split("///")
                parameters = [i.split("|||") for i in parameters]
            else:
                parameters = str(i[4]).split("|||")

            p_s_r_load_list.addItem(f"{name}: {req_type}  TO   {site}  scraping the elements {elements}     with request parameters   {parameters}")

def load_preset_into_fields():
    preset_to_load = p_s_r_load_list.currentItem().text()
    preset_to_load = load_preset(preset_name=preset_to_load.split(':')[0])

    # clear all the lists to prepare them for this sole scrape
    site_list.clear()
    elements_list.clear()
    payloads_list.clear()

    # add the site to the list
    site_list.append({'url': preset_to_load[1], 'request type': preset_to_load[2]})

    # add the elements to the list
    elements_to_add:str = preset_to_load[3]
    # split it first based on diffrerent elements
    elements_to_add = elements_to_add.split("/|\\")
    # create the actual list that will be sent
    actual_elements_to_add = []
    # iterate over the list of elements
    for i in elements_to_add:
        # split it to get the name, attr, and attr value
        i = i.split("|")
        # create a dictionary similiar to the original
        d = {'name': i[0],
             'attribute': i[1],
             'attribute value': i[2],
             'for site': preset_to_load[1]}
        
        actual_elements_to_add.append(d)

    # add the parameters to the list (again the parameters have more complexity so a seperate function for them)
    parameters_inverse_cleaned = inverse_of_web_parameter_formatting(preset_to_load[4], url=preset_to_load[1])

    # add the elements and the parameters
    for i in parameters_inverse_cleaned:
        payloads_list.append(i)
    for i in actual_elements_to_add:
        elements_list.append(i)
    
    display_final_button()

    alert.setText("Info")
    alert.setInformativeText("All data has been set. Dont try to view it, because you probably wont be able to see it. Just press 'Yes' in the final step")
    alert.exec_()

def delete_preset():
    preset = p_s_r_load_list.currentItem().text()
    preset_index = p_s_r_load_list.currentRow()
    preset = preset.split(": ")[0]
    
    delete_presets(preset_name=preset)
    p_s_r_load_list.takeItem(preset_index)
#------------------------------------------------------------------------------------------
# generic function that adds data to the lists. currently no function to remove
def add_to_list(which_list):
    if which_list == 'url':
        url = s_a_p.text()
        req_type = s_a_p_req_type.currentText()
        # ask user to select a method
        if req_type == 'METHOD':
            alert.setText('Error')
            alert.setInformativeText('No request type was specified for the URL. Please select a request type.')
            alert.exec_()
        elif url == '':
            alert_url.setText('Error')
            alert_url.setInformativeText('No URL was provided. Please enter a URL')
            alert_url.exec_()
        else:
            s_a_p.clear()
            url_data = {
                'url': url,
                'request type': req_type
            }
            site_list.append(url_data)

            # append to the main list   
            s_a_p_list.addItem(f"{site_list[-1]['url']}      {site_list[-1]['request type']}")
            
            # append to other required lists
            w_r_p_site.addItem(f"{site_list[-1]['url']}")
            e_t_s_for_site.addItem(f"{site_list[-1]['url']}")
            s_p_a_url_selection.addItem(f"{site_list[-1]['url']}")

    elif which_list == 'element':
        # get the element values
        for_site_e = e_t_s_for_site.currentText()
        element_name = e_t_s_elem.text().lower()
        element_attribute = e_t_s_attrs.text().lower()
        element_attributes_values = e_t_s_attrs_values.text()

        # ask user to select the site this element belongs to
        if for_site_e == 'Select site this element belongs to':
            alert.setText('Error')
            alert.setInformativeText('Please select a site this element belongs to')
            alert.exec_()
        else:
            e_t_s_elem.clear()
            e_t_s_attrs.clear()
            e_t_s_attrs_values.clear()

            elem_data = {
                    'name': element_name,
                    'attribute': element_attribute,
                    'attribute value': element_attributes_values,
                    'for site': for_site_e
            }
            
            # append to main list
            elements_list.append(elem_data)
        
            # append to other required lists
            e_t_s_list.addItem(f"{elements_list[-1]['name']}: {elements_list[-1]['attribute']}->{elements_list[-1]['attribute value']} FOR {elements_list[-1]['for site']}")

    elif which_list == 'payload':
        # get the parameters values
        for_site_p = w_r_p_site.currentText()
        payload_type = w_r_p_select.currentText().lower()
        parameter = w_r_p_add_param.text()
        parameter_value = w_r_p_add_param_value.text()
        
        # ask user to select a site to add the parameter to if they did not
        if for_site_p == 'Select Site':
            alert.setText('Error')
            alert.setInformativeText('Please select a site to send this payload along with')
            alert.exec_()
        else:
            w_r_p_add_param.clear()
            w_r_p_add_param_value.clear()

            if payload_type == 'no parameter' and parameter != '':
                alert.setText("Error")
                alert.setInformativeText("Type is 'No parameter' with parameters being passed?")
                alert.exec_()
            else:
                payl_data = {
                    'for site': for_site_p,
                    'type': payload_type,
                    'param': parameter,
                    'param value': parameter_value
                }

                payloads_list.append(payl_data)

                w_r_p_list.addItem(f"{str(payloads_list[-1]['type']).upper()}: {payloads_list[-1]['param']}->{payloads_list[-1]['param value']} FOR {payloads_list[-1]['for site']}")
    
    elif which_list == 'proxies':
        # get the proxy and the url to which it should belong to
        proxy = s_p_a_adding_box.text()
        proxy_url = s_p_a_url_selection.currentText()
        
        # not store empty data
        if proxy.strip() == '':
            alert.setText('Error')
            alert.setInformativeText("Please specify a proxy")
            alert.exec_()
        elif proxy_url == 'Select a site':
            alert.setText('Error')
            alert.setInformativeText("Please specify a URL this proxy belongs to")
            alert.exec_()
        # after all checks are passed, store the data in both visual and backend lists
        else:
            proxy_data = {
                'for site': proxy_url,
                'proxy': proxy
            }

            proxies_list.append(proxy_data)

            s_p_a_list.addItem(f"{proxy} FOR {proxy_url}")
            pass

# functions to edit the added list of items
def edit_url_list_item():
    selected_item_row = s_a_p_list.currentRow()
    if selected_item_row != -1:
        value, _ = list_item_editor.getText(display_frame, "Edit List Item", "Edit the selected URL; seperate url and request type by using a '|' character like: http://www.somesite.com|GET. even if you wish to only change one aspect of the data, you must reenter the others as well")

        if "|" in value:
            value = value.split('|')

            site_list[selected_item_row]['url'] = value[0]
            site_list[selected_item_row]['request type'] = value[1].upper()


            s_a_p_list.item(selected_item_row).setText("      ".join(i for i in value))

            e_t_s_for_site.removeItem(selected_item_row+1)
            e_t_s_for_site.addItem(value[0])

            w_r_p_site.removeItem(selected_item_row+1)
            w_r_p_site.addItem(value[0])
        else:
            alert.setText("Error")
            alert.setInformativeText("Please declare the '|' divider of url and request type")
            alert.exec_()
    
    else:

    #except AttributeError:
        alert.setText("Error")
        alert.setInformativeText("Please select an item to edit")
        alert.exec_()


def edit_element_list_item():
        selected_item_row = e_t_s_list.currentRow()
        value, _ = list_item_editor.getText(display_frame, "Edit List Item", "Edit the selected element; seperate name, attribute and attribute value by using colons like name:attribute:attribute value:for_site. Even if you wish to only edit one aspect, you must reenter all the other values")

        if ":" in value:
            value = value.split(':')

            elements_list[selected_item_row]['name'] = value[0]
            elements_list[selected_item_row]['attribute'] = value[1]
            elements_list[selected_item_row]['attribute value'] = value[2]
            elements_list[selected_item_row]['for site'] = value[3]

            
            e_t_s_list.item(selected_item_row).setText(f"{elements_list[selected_item_row]['name']}: {elements_list[selected_item_row]['attribute']}->{elements_list[selected_item_row]['attribute value']} FOR {elements_list[selected_item_row]['for site']}")
        else:
            alert.setText("Error")
            alert.setInformativeText("Please declare the ':' divider of the element name, attribute, attribute value and the site it belongs to")
            alert.exec_()


def edit_parameter_list_item():
        selected_item_row = w_r_p_list.currentRow()

        value, _ = list_item_editor.getText(display_frame, "Edit List Item", "Edit the selected payload; seperate the key and value by using the | seperator like so: type|key|value|for_site. Even if you want to change only one thing, you must reenter the other as well.")

        if '|' in value:
            value = value.split("|")

            payloads_list[selected_item_row]['type'] = value[0].capitalize()
            payloads_list[selected_item_row]['param'] = value[1]
            payloads_list[selected_item_row]['param value'] = value[2]
            payloads_list[selected_item_row]['for site'] = value[3]

            w_r_p_list.item(selected_item_row).setText(f"{str(payloads_list[selected_item_row]['type']).upper()}: {payloads_list[selected_item_row]['param']}->{payloads_list[selected_item_row]['param value']} FOR {payloads_list[selected_item_row]['for site']}")
        else:
            alert.setText("Error")
            alert.setInformativeText("Please declare the '|' divider of the parameter type, key, value and the site it goes with")
            alert.exec_()


# function to delete the list items from any of the 3 lists
def delete_list_item(which_list:str):
    if which_list == 'site':
        curr_i = s_a_p_list.currentRow()
        i = s_a_p_list.takeItem(curr_i)
        i = i.text()
        i = i.split("      ")
        i = {"url": i[0], "request type": i[1]}
        e_t_s_for_site.removeItem(curr_i+1)
        w_r_p_site.removeItem(curr_i+1)
        site_list.remove(i)

    # element one is truly confusing
    elif which_list == 'element':
        curr_i = e_t_s_list.currentRow()
        i = e_t_s_list.takeItem(curr_i)
        i = i.text()
        i = i.split(": ")
        i[1] = i[1].split("->")
        i[1][1] = i[1][1].split(" FOR ")
        i = {'name': i[0], 'attribute': i[1][0], 'attribute value': i[1][1][0], 'for site': i[1][1][1]}
        # commented out this print statement, which shows why there are so many lists
        elements_list.remove(i)

# get the response of the element error. if user wants to continue just run the script. else redirect user back to element adding section
def get_elem_error_response(i):
    if i.text() == '&Yes':
        r = run(url_list=site_list, element_list=elements_list, payload_list=payloads_list, nullify_elem_error=True)
        # handling the case where a post request is trying to be sent without any payloads/web parameters. What are they trying to POST?
        if r == 'show post_without_payload error':
            alert_payload.setText('Error')
            alert_payload.setInformativeText('A POST request is trying to be sent without any payloads. Please define a payload to be sent with the POST request')
            alert_payload.exec_()
        else:
            alert.setText("Scrape has started")
            alert.setInformativeText("The scrape has started in a seperate thread. You can close this app if you wish, the results will be saved in the data folder")
            alert.exec_()
            display_set_site_controls()
    elif i.text() == '&No':
        display_set_elements_to_scrape()



# the function that actually starts the scraping
def start_scrape():
    r = run(url_list=site_list, element_list=elements_list, payload_list=payloads_list)

    # handle the case where no urls are added. what are they trying to scrape?
    if r == 'show nan_url error':
        alert_url.setText('Error')
        alert_url.setInformativeText('No URLs were provided. Please enter atleast 1 URL to scrape')
        alert_url.exec_()
    # handle the case where no elements are defined. ask the user if they wish to scrape the entire site since that is basically what will happen
    elif r == 'show nan_elems error':
        alert_elements.setText('Error')
        alert_elements.setInformativeText('No elements were provided. This will mean the program will scrape the entire content of the page. Do you want to proceed?')
        alert_elements.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        alert_elements.buttonClicked.connect(get_elem_error_response)
        alert_elements.exec_()
    # handle the case where the user forgot to define any parameters, including the 'no paraeters'
    elif r == 'show nan_payls error':
        alert_payload.setText('Error')
        alert_payload.setInformativeText('No payloads were specified. If you wish to scrape without any web parameters, select the "No parameters" option for the site in payloads setting option')
        alert_payload.exec_()
    else:
        alert.setText("Scrape has started")
        alert.setInformativeText("The scrape has started in a seperate thread. You can close this app if you wish, the results will be saved in the data folder")
        alert.exec_()
        display_set_site_controls()


    # handling the case where a post request is trying to be sent without any payloads/web parameters. What are they trying to POST?
    if r == 'show post_without_payload error':
        alert_payload.setText('Error')
        alert_payload.setInformativeText('A POST request is trying to be sent without any payloads. Please define a payload to be sent with the POST request')
        alert_payload.exec_()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


site_list = []
elements_list = []
payloads_list = []
proxies_list = []


app = QApplication([])

root = QWidget()
root.setFixedSize(800, 500)
root.setWindowTitle('Web Scraper')

control_frame = QFrame(root)
display_frame = QFrame(root)

control_frame.setFixedSize(300, 470)
control_frame.move(5, 10)
control_frame.setStyleSheet('')

display_frame.setFixedSize(480, 470)
display_frame.move(310, 10)
display_frame.setStyleSheet('')

h = QLabel(control_frame)
h.setText('<h2>Web Scraper</h2>')
h.move(10, 5)

set_site_button = QPushButton(control_frame)
set_site_button.setFixedSize(170, 50)
set_site_button.move(10, 40)
set_site_button.setText("Set the Site to scrape")
set_site_button.clicked.connect(lambda: display_set_site_controls())

set_attrs_button = QPushButton(control_frame)
set_attrs_button.setFixedSize(170, 50)
set_attrs_button.move(10, 100)
set_attrs_button.setText("Set the elements to scrape")
set_attrs_button.clicked.connect(lambda: display_set_elements_to_scrape())

payload_setting_show_button = QPushButton(control_frame)
payload_setting_show_button.setFixedSize(170, 50)
payload_setting_show_button.move(10, 160)
payload_setting_show_button.setText("Set Payloads or\nHeaders for scrape")
payload_setting_show_button.clicked.connect(lambda: display_set_payloads_controls())

preset_manager_show_button = QPushButton(control_frame)
preset_manager_show_button.setFixedSize(170, 50)
preset_manager_show_button.move(10, 220)
preset_manager_show_button.setText("Set/Run Presets")
preset_manager_show_button.clicked.connect(lambda: display_presets_controls())

proxy_setting_show_button = QPushButton(control_frame)
proxy_setting_show_button.setFixedSize(170, 50)
proxy_setting_show_button.move(10, 280)
proxy_setting_show_button.setText("Set Proxies")
proxy_setting_show_button.clicked.connect(lambda: display_proxy_controls())

# final display and confirm the user wants to start scrape
final_send_button = QPushButton(control_frame)
final_send_button.setFixedSize(170, 50)
final_send_button.move(10, 340)
final_send_button.setText("Start Scraping")
final_send_button.clicked.connect(lambda: display_final_button())

# A button to reset the app's data
reset_app_data = QPushButton(control_frame)
reset_app_data.setText("Reset App Data")
reset_app_data.move(10, 400)
reset_app_data.setFixedSize(170, 50)
reset_app_data.clicked.connect(lambda: reset_app())


#---------------------------------------------------
# set site adding control panel widgets
s_a_p_label = QLabel(display_frame)
s_a_p_label.setText("Add the URLS to scrape")
s_a_p_label.setFont(QFont("Segoe UI", 13))
s_a_p_label.move(10, 30)

s_a_p = QLineEdit(display_frame)
s_a_p.move(10, 60)
s_a_p.setFixedSize(200, 20)
s_a_p.setFont(QFont('Segoe UI'))
s_a_p.setPlaceholderText('URL')

s_a_p_req_type = QComboBox(display_frame)
s_a_p_req_type.addItems(['METHOD', 'GET', 'POST'])
s_a_p_req_type.setFixedSize(90, 20)
s_a_p_req_type.setFont(QFont('Segoe UI', 9))
s_a_p_req_type.move(220, 60)

s_a_p_button = QPushButton(display_frame)
s_a_p_button.setText('+')
s_a_p_button.move(315, 58)
s_a_p_button.setFixedSize(50, 24)
s_a_p_button.clicked.connect(lambda: add_to_list('url'))


s_a_p_list = QListWidget(display_frame)
s_a_p_list.setGeometry(10, 85, 294, 360)
s_a_p_list.addItems(site_list)

s_a_p_list_edit_button = QPushButton(display_frame)
s_a_p_list_edit_button.setFixedSize(90, 30)
s_a_p_list_edit_button.move(310, 100)
s_a_p_list_edit_button.setText("Edit List Item")
s_a_p_list_edit_button.clicked.connect(lambda: edit_url_list_item())

s_a_p_list_delete_button = QPushButton(display_frame)
s_a_p_list_delete_button.setFixedSize(90, 30)
s_a_p_list_delete_button.move(310, 140)
s_a_p_list_delete_button.setText("Delete List Item")
s_a_p_list_delete_button.clicked.connect(lambda: delete_list_item(which_list='site'))

s_a_p_label.hide()
s_a_p.hide()
s_a_p_req_type.hide()
s_a_p_button.hide()
s_a_p_list.hide()
s_a_p_list_edit_button.hide()
s_a_p_list_delete_button.hide()

#---------------------------------------------------
# set elements to scrape adding control panel widgets
e_t_s_label = QLabel(display_frame)
e_t_s_label.setText("Add elements to scrape")
e_t_s_label.setFont(QFont('Segoe UI', 13))
e_t_s_label.move(10, 30)

e_t_s_elem = QLineEdit(display_frame)
e_t_s_elem.move(10, 60)
e_t_s_elem.setFixedSize(70, 20)
e_t_s_elem.setFont(QFont('Segoe UI'))
e_t_s_elem.setPlaceholderText('Element')

e_t_s_attrs = QLineEdit(display_frame)
e_t_s_attrs.move(90, 60)
e_t_s_attrs.setFixedSize(90, 20)
e_t_s_attrs.setFont(QFont('Segoe UI'))
e_t_s_attrs.setPlaceholderText('Attribute')

e_t_s_attrs_values = QLineEdit(display_frame)
e_t_s_attrs_values.move(190, 60)
e_t_s_attrs_values.setFixedSize(200, 20)
e_t_s_attrs_values.setFont(QFont('Segoe UI'))
e_t_s_attrs_values.setPlaceholderText('Attribute Values')

e_t_s_add_button = QPushButton(display_frame)
e_t_s_add_button.move(400, 59)
e_t_s_add_button.setText('+')
e_t_s_add_button.clicked.connect(lambda: add_to_list('element'))

e_t_s_for_site = QComboBox(display_frame)
e_t_s_for_site.move(10, 89)
e_t_s_for_site.setFixedSize(300, 20)
e_t_s_for_site.addItem('Select site this element belongs to')

e_t_s_list = QListWidget(display_frame)
e_t_s_list.setGeometry(10, 115, 380, 350)

e_t_s_list_edit_button = QPushButton(display_frame)
e_t_s_list_edit_button.setFixedSize(90, 30)
e_t_s_list_edit_button.move(390, 130)
e_t_s_list_edit_button.setText("Edit List Item")
e_t_s_list_edit_button.clicked.connect(lambda: edit_element_list_item())

e_t_s_list_delete_button = QPushButton(display_frame)
e_t_s_list_delete_button.setFixedSize(90, 30)
e_t_s_list_delete_button.move(390, 170)
e_t_s_list_delete_button.setText("Delete List Item")
e_t_s_list_delete_button.clicked.connect(lambda: delete_list_item(which_list='element'))

e_t_s_label.hide()
e_t_s_elem.hide()
e_t_s_attrs.hide()
e_t_s_attrs_values.hide()
e_t_s_for_site.hide()
e_t_s_add_button.hide()
e_t_s_list.hide()
e_t_s_list_edit_button.hide()
e_t_s_list_delete_button.hide()

#---------------------------------------------------
# widgets for setting payloads or other web request parameters
w_r_p_label = QLabel(display_frame)
w_r_p_label.setText('Add request parameters or data')
w_r_p_label.move(10, 30)
w_r_p_label.setFont(QFont('Segoe UI', 13))

w_r_p_site_label = QLabel(display_frame)
w_r_p_site_label.setText('For site:')
w_r_p_site_label.setFont(QFont('Segoe UI', 9))
w_r_p_site_label.move(10, 60)

w_r_p_site = QComboBox(display_frame)
w_r_p_site.addItem('Select Site')
w_r_p_site.move(60, 58)
w_r_p_site.setFixedSize(300, 20)
w_r_p_site.setFont(QFont("Segoe UI", 8))

w_r_p_select_label = QLabel(display_frame)
w_r_p_select_label.setText('Select content type:')
w_r_p_select_label.move(10, 90)
w_r_p_select_label.setFont(QFont('Segoe UI', 9))

w_r_p_select = QComboBox(display_frame)
w_r_p_select.addItems(['Payload', 'Headers', 'Files', 'JSON', 'No Parameter'])
w_r_p_select.move(120, 88)
w_r_p_select.setFixedHeight(20)
w_r_p_select.setFont(QFont('Arial', 8))

w_r_p_add_param = QLineEdit(display_frame)
w_r_p_add_param.move(10, 120)
w_r_p_add_param.setPlaceholderText('Name/Key')
w_r_p_add_param.setFont(QFont('Segoe UI'))

w_r_p_add_param_value = QLineEdit(display_frame)
w_r_p_add_param_value.move(140, 120)
w_r_p_add_param_value.setFixedWidth(250)
w_r_p_add_param_value.setPlaceholderText('Value')

w_r_p_add_button = QPushButton(display_frame)
w_r_p_add_button.setText('+')
w_r_p_add_button.setFont(QFont('Segoe UI'))
w_r_p_add_button.setFixedWidth(40)
w_r_p_add_button.move(400, 119)
w_r_p_add_button.clicked.connect(lambda: add_to_list('payload'))

w_r_p_list = QListWidget(display_frame)
w_r_p_list.setGeometry(10, 155, 380, 300)

w_r_p_list_edit = QPushButton(display_frame)
w_r_p_list_edit.setFixedSize(80, 30)
w_r_p_list_edit.setText("Edit List Item")
w_r_p_list_edit.move(390, 170)
w_r_p_list_edit.clicked.connect(lambda: edit_parameter_list_item())

w_r_p_label.hide()
w_r_p_site_label.hide()
w_r_p_site.hide()
w_r_p_select_label.hide()
w_r_p_select.hide()
w_r_p_add_param.hide()
w_r_p_add_param_value.hide()
w_r_p_add_button.hide()
w_r_p_list.hide()
w_r_p_list_edit.hide()

#---------------------------------------------------------
# widgets for the preset setting/loading and running
p_s_r_label = QLabel(display_frame)
p_s_r_label.setText("Set/Run Presets")
p_s_r_label.move(10, 30)
p_s_r_label.setFont(QFont('Segoe UI', 13))

p_s_r_create_label = QLabel(display_frame)
p_s_r_create_label.setText("Create a Preset\n(Presets are created from the data you have entered\nabove in the previous fields)")
p_s_r_create_label.move(10, 70)
p_s_r_create_label.setFont(QFont('Segoe UI', 10))

p_s_r_create_button = QPushButton(display_frame)
p_s_r_create_button.setText("Create a preset")
p_s_r_create_button.setFixedWidth(100)
p_s_r_create_button.move(10, 130)
p_s_r_create_button.clicked.connect(lambda: create_preset_())

p_s_r_load_label = QLabel(display_frame)
p_s_r_load_label.setText("Load a preset\n(This will load the selected preset's data, and override\nany data you have entered above. To run this preset\nsimply run the scrape like you would normally)")
p_s_r_load_label.move(10, 180)
p_s_r_load_label.setFont(QFont('Segoe UI', 10))

# this button loads the presets from the database
p_s_r_load_button = QPushButton(display_frame)
p_s_r_load_button.setText("Load presets\nfrom database")
p_s_r_load_button.move(370, 260)
p_s_r_load_button.setFixedWidth(80)
p_s_r_load_button.clicked.connect(lambda: loading_all_the_presets())

p_s_r_load_list = QListWidget(display_frame)
p_s_r_load_list.setGeometry(10, 260, 350, 200)

# this button loads the presets into the required fields
p_s_r_load_into_run_button = QPushButton(display_frame)
p_s_r_load_into_run_button.setText("Load this\npreset")
p_s_r_load_into_run_button.move(370, 300)
p_s_r_load_into_run_button.setFixedWidth(80)
p_s_r_load_into_run_button.clicked.connect(lambda: load_preset_into_fields())

# this button deletes the presets that the user wants
p_s_r_delete_preset_button = QPushButton(display_frame)
p_s_r_delete_preset_button.setText("Delete this\npreset")
p_s_r_delete_preset_button.move(370, 340)
p_s_r_delete_preset_button.setFixedWidth(80)
p_s_r_delete_preset_button.clicked.connect(lambda: delete_preset())

p_s_r_label.hide()
p_s_r_create_label.hide()
p_s_r_create_button.hide()
p_s_r_load_label.hide()
p_s_r_load_button.hide()
p_s_r_delete_preset_button.hide()
p_s_r_load_list.hide()
p_s_r_load_into_run_button.hide()

#---------------------------------------------------
# widgets for proxies adding
s_p_a_title = QLabel(display_frame)
s_p_a_title.move(10, 30)
s_p_a_title.setFont(QFont("Segoe UI", 13))
s_p_a_title.setText("Add Proxies")

s_p_a_adding_box_label = QLabel(display_frame)
s_p_a_adding_box_label.setText("Add a proxy")
s_p_a_adding_box_label.setFont(QFont('Segoe UI', 10))
s_p_a_adding_box_label.move(10, 80)

s_p_a_adding_box = QLineEdit(display_frame)
s_p_a_adding_box.move(90, 80)
s_p_a_adding_box.setFixedWidth(300)

s_p_a_url_label = QLabel(display_frame)
s_p_a_url_label.setText("Select the URL this proxy belongs to:")
s_p_a_url_label.move(10, 110)
s_p_a_url_label.setFont(QFont("Segoe UI", 10))

s_p_a_url_selection = QComboBox(display_frame)
s_p_a_url_selection.setFixedSize(270, 20)
s_p_a_url_selection.setFont(QFont('Segoe UI', 8))
s_p_a_url_selection.addItem("Select a site")
s_p_a_url_selection.move(10, 130)

s_p_a_adding_button = QPushButton(display_frame)
s_p_a_adding_button.setText("+")
s_p_a_adding_button.setFixedWidth(70)
s_p_a_adding_button.move(290, 129)
s_p_a_adding_button.clicked.connect(lambda: add_to_list('proxies'))

s_p_a_list = QListWidget(display_frame)
s_p_a_list.setGeometry(10, 160, 350, 290)


s_p_a_title.hide()
s_p_a_adding_box_label.hide()
s_p_a_adding_box.hide()
s_p_a_url_label.hide()
s_p_a_url_selection.hide()
s_p_a_adding_button.hide()
s_p_a_list.hide()

#---------------------------------------------------
# wigdets to confirm to start scrape after showing the scrape data

ask = QLabel(display_frame)
ask.move(10, 30)
ask.setText('Start Scrape?')
ask.setFont(QFont('Segoe UI', 13))

show_site_list_l = QLabel(display_frame)
show_site_list_l.setText('Sites')
show_site_list_l.move(10, 80)
show_site_list_l.setFont(QFont('Segoe UI', 10))

show_site_list = QListWidget(display_frame)
show_site_list.setGeometry(10, 100, 190, 260)

show_elems_list_l = QLabel(display_frame)
show_elems_list_l.move(220, 80)
show_elems_list_l.setFont(QFont('Segoe UI', 10))
show_elems_list_l.setText('Elements')

show_elems_list = QListWidget(display_frame)
show_elems_list.setGeometry(220, 100, 190, 260)

yes_button = QPushButton(display_frame)
yes_button.setFixedSize(140, 30)
yes_button.setText('Yes')
yes_button.move(60, 390)
yes_button.setStyleSheet('background: lightgreen;')
yes_button.clicked.connect(start_scrape)

no_button = QPushButton(display_frame)
no_button.setFixedSize(140, 30)
no_button.setText('No, modify')
no_button.move(220, 390)
no_button.setStyleSheet('background: pink')
no_button.clicked.connect(lambda: display_set_site_controls())

ask.hide()
show_site_list_l.hide()
show_site_list.hide()
show_elems_list_l.hide()
show_elems_list.hide()
yes_button.hide()
no_button.hide()

#-----------------------------------------------------

alert = QMessageBox()
alert_url = QMessageBox()
alert_elements = QMessageBox()
alert_payload = QMessageBox()
list_item_editor = QInputDialog
preset_name_asker = QInputDialog
root.show()

if __name__ == '__main__':
    app.exec_()