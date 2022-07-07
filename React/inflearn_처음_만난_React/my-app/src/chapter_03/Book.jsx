import React from "react";

// 짧고 간결하다
// JSX는 React 공식에서 사용을 권장한다
function Book(props) {
    return (
        <div>
            <h1>{`이 책의 이름은 ${props.name}입니다.`}</h1>
            <h2>{`이 책은 총 ${props.numOfPage}페이지로 이루어져 있습니다.`}</h2>
        </div>
    )
}

// JSX 없이 React로만 작성할 때
// 너무 길다
// function Book(props) {
//     return React.createElement(
//         'div',
//         null,
//         [
//             React.createElement(
//                 'h1',
//                 null,
//                 `이 책의 이름은 ${props.name} 입니다`
//             ),
//             React.createElement(
//                 'h2',
//                 null,
//                 `이 책은 총 ${props.numOfPage}페이지로 이루어져 있습니다.`
//             )
//         ]
//     )
// }

export default Book;