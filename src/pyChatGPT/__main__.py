from pyChatGPT import ChatGPT
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    while True:
        authMethod = input('token')
        if authMethod.lower() == 'token':
            session_token = input('eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..4xl7L9g1zXGBPWYF.zNTXA8MQ6RvFj8TsfjsXQ4S8vsCp2gSGVMO8FhppqVgCRsZ0vWQCEIgbZzUOOYXTE_Ltqyg5qO3SJVsXsWcH6cVN_jjofX5HPTCuT2TsiuRwqjV5oMlS0fWyoTVJHjH776sUy4kJzq4K25Q01jtXbuJxNq1kLKfyhMYVu_FaUn2Q4L73IXOOr0H2H-PLqT7BO8A4nmi_F0mqrY_LTnVX2rY4iMK1Nu5fPy2Uj4OqvObmD9wXpfpRBSXLBaKxzlCdQ1sDJLT3hEVzI5SWln4H0qU4b22aWnIXmrfxM4i-YliMpsTgQ1ZcSaxiM4SIcS4ez_QTZ18Qb7s7rcCGStFZsbKT-R80OhowQhjHu4gBC_97IQIfcE6SrhnjR7Jc92Fii3LGzMjtqmEo5FsD9r4h157y30d7ayoWkt0-pnCMj9aglzEPfQb5YEdgn_-awz-9DG1rVpxbLDCW1DbGZRQxL6OTFMvhVXF11eaUYs5NMhsvt0fumHl4t-ZL5IVt0yrVT64emM5Rg0sEau_Doala5CmaigeuAf4CjTrevXCc5RTYaBIQnYJMQYYr085o-gIkKwqHIaZeXUBl2aNobA8n2bW0QNw5MaKMypGKPIdoc97DH-jnke-Y3gZ1mQL9jcaj3a8emo_4-3rtry5vUsykt91yGO5XNWiuGRqW1eScSKcUshU-8yjLWuijmDkBgnor3LTma8pUD0xW9XVvnRHA01_2lsuvXyRrWMVWTKMTxr3c2D9c9WX6TWiiODq4dg-yWgGSg1M3OCIkF9ebVmp44Ra6SO42QXxb_Cduyn5sNIY_IhFGGRnlTxBZlYmU_7h_g4jREmPM2c8dJW7WT0O2wmo8TlXqjZap3MDtmgK6w_gARAFNoT6XOZhHyXF83-sns0962zbWzAigJ6MmC9adDbHOZdUOM5FQaY8o-Mx7oDCYnKkV2jnGQowWTkYlK3ko-07nxVps-sezAyHOQLakqhHkL_B0ND0OfxkebvOFOjn44nFbUqrS6qCGR1_lCz0G6OIzijbCFGpAkxo-Gi_AbPFamiY18HQ1GcR6wwsPjWmaGU-ErwtnPZxm7VFkCTZMDUTNchNlBSsfnqlCJY8lSIYq1YI15t8lSa_RJb_JI6fc9eDDzm_YqmVg5Ph2AWslhBSIfj-6KtpPTfiMlBc2Kw84KNK8KrusbQiSYz8k7BeJKX9iuk_IW-1Fo-TbNW_a0MaXcltPVI5XRqN6Sl5XdwIWF6zafRUoFwWgXj14lf53k6tzTECv-Fm_qThJVznGPsUAU4-c3zJjMMOcr0CuYsajmxb_YxBmzvPVthO7E8vDpC01g6I9FVwo8lTdXiZgIDWH5w8PqsUn-_v8E9GMnHoTl1jg7xNVWx1AYs-LQza1G3g2ffeNoaHsbxLRnPSmjuOFYxcXTdIPkqKVsU4CcGkzsL3tnxjlVn6Lo7VzHziVWQ-cpln882-uEGhK_kkkdaMxMcbdb_HWcLBt7Ba5BUXXRECL7yQeBAyq3FSv70sVVG79HqHATriO1pk0IBuRsW2roBe-6lU8EDf3EoO_ZSoWAnFdLyXEkRWyzrrx7uv72yqnJnBhztOCVerCk-IGjslcO--WUaqy2UgYf7vyqZYuks-POba57n5WPMzuNKpIrCUjFiSJmJalpssG52xU3-VhzPeANxCdX1M8V6PV-ewr58w4XQ8ZKy3_XhLGGpxYSqSexFq4Bk4Ssv63kcqFtorAAzXxQ1BsIkFhK2SL-niq8_rBQM1K7QDoD0jB7aGi2QzRoWbylB1Vorku6kjOm51fJdoeixM_q6L27L5UxPb19LmvaLAAZX6H3NHofFQf1TDKbf1gMqfe0KfaLWYSLPaHphhXaEq27idnCCUbOSxE0eji0G6f-NlAxw8LfoDI_QQ64ePVobEN71nVs0mRFa1lVO40BHvxjv83SDsQgwb5Df8xTlDFyvOWeu5qPjkmjJ1V_CRJa8zT8S1U-CqqonZZi3hbl7c64f5omVnCRXthju3vB3PDPAmw_YklhK7fX-yMAepTruYYyuf4Omcssam14GZjC5mSd2zwQC7sIZYzJCPjaZem5BSLlNJa7ieagUATQlxwRddp6WUyh4NTecEJYAed0cMiMRrfDszftrHzx-Ux3agP1bUoxHIldzHUi4KRyAYLS9DKMJh0oMaWi8CEJAa6Njlhjq9NKysrN11-YzNccT0C9CvkqiZP58S4WJwCf7ZXwOc4WTvK4UCEwzotZrtheuZDRd0Ivrq8khXfIwtIZf8gxGsAIhS_9d1lN7Ln66oHx1fA57Q.qvtsdciGAdH0Vp7cp_cyWA')
            chat = ChatGPT(session_token)
            break
        elif authMethod.lower() == 'email':
            email = input('Please enter your email: ')
            password = input('Please enter your password: ')
            chat = ChatGPT(email, password)
            break
        clear_screen()

    clear_screen()
    print(
        'Conversation started. Type "reset" to reset the conversation. Type "reauth" to reauthenticate.'
    )
    while True:
        prompt = input('\nYou: ')
        if prompt.lower() == 'reset':
            chat.reset_conversation()
            clear_screen()
            print(
                'Conversation started. Type "reset" to reset the conversation. Type "reauth" to reauthenticate.'
            )
            continue
        if prompt.lower() == 'reauth':
            chat.refresh_auth()
            print('Reauthenticated.')
            continue
        print('\nChatGPT:', end=' ')
        response = chat.send_message(prompt)
        print(response['message'])
