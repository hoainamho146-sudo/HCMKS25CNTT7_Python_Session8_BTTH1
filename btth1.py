video_description = ""
hashtags = []

while True:
    print("+================================================+")
    print("|        HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK        |")
    print("+================================================+")
    print("|  1. Nhập và phân tích thông tin video          |")
    print("|  2. Chuẩn hóa tên tài khoản                    |")
    print("|  3. Kiểm tra tính hợp lệ của hashtag           |")
    print("|  4. Tìm kiếm và thay thế từ khóa trong mô tả   |")
    print("|  5. Thoát chương trình                         |")
    print("+================================================+")

    choice = input("> Mời bạn chọn chức năng (1-5): ")

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ")
        continue

    choice = int(choice)

    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ")
        continue

    if choice == 1:
        account = input("Nhập tên tài khoản: ")

        if account.strip() == "":
            print("Tên tài khoản không được rỗng")
            continue

        title = input("Nhập tiêu đề video: ")
        description = input("Nhập mô tả video: ")

        if description.strip() == "":
            print("Mô tả video không được rỗng")
            continue

        hashtag_input = input("Nhập danh sách hashtag (cách nhau bởi dấu phẩy): ")

        account = account.strip()
        title = title.strip().title()
        description = description.strip()

        video_description = description

        hashtags = []
        for tag in hashtag_input.split(","):
            tag = tag.strip()
            if tag != "":
                hashtags.append(tag)

        print("\n===== BÁO CÁO THỐNG KÊ =====")
        print("Tên tài khoản:", account)
        print("Tiêu đề video:", title)
        print("Mô tả video:", description)
        print("Độ dài mô tả:", len(description))
        print("Số lượng từ:", len(description.split()))
        print("Danh sách hashtag:", hashtags)
        print("Số lượng hashtag:", len(hashtags))
        print("Mô tả chữ thường:", description.lower())
        print("Mô tả chữ hoa:", description.upper())

    elif choice == 2:
        account = input("Nhập tên tài khoản: ")

        if account.strip() == "":
            print("Tên tài khoản không được rỗng")
            continue

        print("Tên tài khoản ban đầu:", account)

        account = account.strip().lower()

        if not account.startswith("@"):
            account = "@" + account

        print("Tên tài khoản chuẩn hóa:", account)

    elif choice == 3:
        hashtag = input("Nhập hashtag cần kiểm tra: ").strip()

        if hashtag == "":
            print("Hashtag không được rỗng")

        elif not hashtag.startswith("#"):
            print("Hashtag phải bắt đầu bằng ký tự #")

        elif " " in hashtag:
            print("Hashtag không được chứa khoảng trắng")

        elif len(hashtag) < 2:
            print("Hashtag phải có ít nhất 2 ký tự")

        else:
            valid = True

            for char in hashtag[1:]:
                if not (char.isalnum() or char == "_"):
                    valid = False
                    break

            if valid:
                print("Hashtag hợp lệ")
                hashtags.append(hashtag)
                print("Đã thêm hashtag vào danh sách hiện tại")
            else:
                print("Hashtag chỉ được chứa chữ cái, chữ số hoặc dấu gạch dưới")

    elif choice == 4:
        if video_description == "":
            print("Chưa có mô tả video")
            continue

        find_word = input("Nhập từ khóa cần tìm: ")
        replace_word = input("Nhập từ khóa thay thế: ")

        count = video_description.count(find_word)

        if count > 0:
            new_description = video_description.replace(find_word, replace_word)

            print("Số lần xuất hiện:", count)
            print("Mô tả sau khi thay thế:")
            print(new_description)
        else:
            print("Không tìm thấy từ khóa trong mô tả")

    elif choice == 5:
        print("Thoát chương trình")
        break
