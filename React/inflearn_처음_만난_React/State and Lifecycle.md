# State and Lifecycle

- 주로 Class Component와 연관된 파트
- 단 State는 function Component에서도 사용하므로 개념을 잘 이해해야함
- Lifecycle은 최근 Class Component의 사용량이 줄어들었으므로 이런 것이 있다는 정도로 이해하면 됨



### State

- React Component의 상태(단 정상/ 비정상 의미의 상태 X) => Component의 데이터

- State = React Component의 변경 가능한 데이터

- State는 개발자가 정의한다

- 렌더링이나 데이터 흐름에 사용되는 값만 state에 포함시켜야함

- state가 변경될 경우 재 렌더링되기 때문에

- 렌더링과 데이터 흐름에 관계 없는 값을 포함하면 불필요한 경우에 컴포넌트가 다시 재 렌더링 => 성능 저하

- 관계 없는 값은  Component의 Instance 필드로 정의하면 된다

- state는 따로 복잡한 형태가 아닌 하나의 JavaScript 객체이다

- ```react
  class LikeButton extends React.Component {
      // constructor(생성자) => 모든 class Component가 가지고 있음 / class가 생성될 때 실행
      // 함수 component는 use state라는 Hook을 이용해 정의
      constructor(props) {
          super(props);
          
  		// 현재 component의 state를 정의하는 부분
          this.state = {
              liked: false
          };
      }
      
      ...
  }
  ```

- state는 직접 수정할 수 없다(사실 가능하지만 하면 안된다) => Component의 렌더링과 관련있기 때문에

- ```react
  // state를 직접 수정 (잘못된 사용법)
  this.state = {
      name: 'Inje'
  };
  
  // setState 함수를 통한 수정 (정상적인 사용법)
  this.setState({
      name: 'Inje'
  });
  ```



### Lifecycle

- React Component의 생명주기(출생 - 인생 - 사망)
- `componentDidMount, componentDidUpdate, componentWillUnmount` => 생명주기에 따라 호출되는 Class Component 함수 => `Lifecycle method`(생명주기 함수)
- 출생(Mounting)
  - 생성자(constructor) 실행, state 정의 => 렌더링
- 인생(Updating)
  - 새로운 Props, setState(), forceUpdate()(강제 업데이트)
- 사망(Unmounting)
  - 상위 컴포넌트에서 현재 컴포넌트를 더 이상 화면에 표시하지 않을 때



## 정리

- Component가 계속 존재하는 것이 아니라, 시간의 흐름에 따라 생성되고 업데이트 되다가 사라진다
- 클래스 Component 뿐만 아니라, 함수 Component에도 해당되는 이야기