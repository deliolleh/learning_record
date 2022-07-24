import React, { useState, useEffect } from "react";
import useCounter from "./useCounter";

const MAX_CAPACITY = 10;

function Accommodate(props) {
    const [isFull, setIsFull] = useState(false);
    const [count, increaseCount, decreaseCount] = useCounter(0);

    useEffect(() => {
        console.log("===============================");
        console.log("useEffect() is called.");
        console.log(`isFull: ${isFull}`);
    });
    // 의존성 배열 X
    // Component가 mount 된 직후에 호출
    // 업데이트가 될 때마다 호출

    useEffect(() => {
        setIsFull(count >= MAX_CAPACITY);
        console.log(`Current count value: ${count}`);
    }, [count]);
    // 의존성 배열 O
    // Component가 mount 된 직후에 호출
    // 이후 Count 값이 바뀔 때마다 호출
    // isFull이라는 State을 통해 용량이 다 찼는지 확인

    return (
        <div style={{padding : 16}}>
            <p>{`총 ${count}명 수용했습니다.`}</p>

            <button onClick={increaseCount} disabled={isFull}>
                입장
            </button>
            <button onClick={decreaseCount}>
                퇴장
            </button>

            {isFull && <p style={{color : "red"}}>정원이 가득찼습니다.</p>}
        </div>
    );
}

export default Accommodate;